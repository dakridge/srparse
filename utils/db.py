import csv
import arrow
import pandas
import sqlite3
from cols import tables

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

conn = sqlite3.connect('surpriseride.db')
conn.text_factory = str
conn.row_factory = dict_factory

# def connect():
#     # connect
#     if not conn:
#         conn = sqlite3.connect('surpriseride.db')

def getCursor():
    # connect()
    cursor = conn.cursor()
    return cursor

def clearTables():
    '''
        Creates our tables
    '''
    cursor = getCursor()
    cursor.executescript('DROP TABLE IF EXISTS orders; DROP TABLE IF EXISTS subscriptions; DROP TABLE IF EXISTS transactions;')
    conn.commit

def importCSVFiles(filesList):
    for file in filesList:
        # load data
        csvData = pandas.read_csv(file['path'], low_memory=False)

        # strip whitespace from headers
        csvData.columns = csvData.columns.str.strip()

        # drop into table
        csvData.to_sql(file['table'], conn)

def getBundleCountsByMonth():
    cursor = getCursor()
    cursor.execute("SELECT placed_at, products FROM orders WHERE products LIKE '%bundle%';")
    bundles = cursor.fetchall()

    bundleCountsByMonth = {}

    for bundle in bundles:
        bundleNames = bundle['products'].split(',')
        for bundleName in bundleNames:
            if 'bundle' in bundleName.lower():

                bundleBuyDate = arrow.get(bundle['placed_at']).to('US/Eastern').format('YYYY-MM')
                if bundleBuyDate in bundleCountsByMonth:
                    bundleCountsByMonth[bundleBuyDate] += 1
                else:
                    bundleCountsByMonth[bundleBuyDate] = 1

    return bundleCountsByMonth

def getBundleCountsByName():
    cursor = getCursor()
    cursor.execute("SELECT products FROM orders WHERE products LIKE '%bundle%';")
    bundles = cursor.fetchall()

    bundleDict = {}

    for bundle in bundles:
        bundleNames = bundle['products'].split(',')
        for bundleName in bundleNames:
            if 'bundle' in bundleName.lower():

                strippedBundleName = bundleName.strip()
                if strippedBundleName in bundleDict:
                    bundleDict[strippedBundleName] += 1
                else:
                    bundleDict[strippedBundleName] = 1

    return bundleDict

def getTotalOrdersByMonth():
    cursor = getCursor()
    cursor.execute("SELECT placed_at, products FROM orders;")
    orders = cursor.fetchall()

    monthDict = {}

    for order in orders:
        orderDate = arrow.get(order['placed_at']).to('US/Eastern').format('YYYY-MM')
        monthDict[orderDate] = monthDict.get(orderDate, 0) + 1
        
    return monthDict

def getSubscriptionsVsEShopOrders():
    '''
        This sums up the number of subscriptions and the number of one-time
        orders in the transactions table. The problem is that it counts each
        subscription renewal as a subscription.
    '''
    cursor = getCursor()
    cursor.execute('''SELECT Products, "Order Date" FROM transactions;''')
    transactions = cursor.fetchall()

    monthDict = {}

    for transaction in transactions:
        transactionProducts = transaction['Products'].split(',')
        orderMonth = arrow.get(transaction['Order Date'], 'MM/DD/YYYY').to('US/Eastern').format('YYYY-MM')

        if orderMonth not in monthDict:
            monthDict[orderMonth] = { 'Subscriptions': 0, 'Eshop': 0 }

        for productName in transactionProducts:
            if 'subscription' in productName.lower():
                monthDict[orderMonth]['Subscriptions'] += 1
            else:
                monthDict[orderMonth]['Eshop'] += 1
        
    return monthDict