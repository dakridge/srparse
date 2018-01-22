# db
import csv
import sqlite3

# functions
from utils import db
from utils import files

'''
    Config
'''
location = '../'


# get the files in the current directory
dirfiles = files.findFiles(location)

# import our files
db.clearTables()
db.importCSVFiles([
    { "table": 'orders', "path": dirfiles['orders']},
    { "table": 'subscriptions', "path": dirfiles['subscriptions']},
    { "table": 'transactions', "path": dirfiles['transactions']}
])

'''
    Outputs
'''

# find bundles - get all rows with the word 'bundle' in it
bundlesByMonth = db.getBundleCountsByMonth()

print '\n\nTotal number of kits sold in bundles'
for date, count in sorted(bundlesByMonth.items()):
    print date + ' - ' + str(count * 3)

ordersByMonth = db.getTotalOrdersByMonth()
print '\n\nTotal number of orders placed'
for date, count in sorted(ordersByMonth.items()):
    print date + ' - ' + str(count)

subscriptionsVsRegularOrdersByMonth = db.getSubscriptionsVsEShopOrders()
print '\n\nSubscriptions Vs EShop Orders by month'

for date, counts in sorted(subscriptionsVsRegularOrdersByMonth.items()):
    print date + ' - Subscriptions: ' + str(counts['Subscriptions']) + ', Eshop: ' + str(counts['Eshop'])