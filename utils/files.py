'''
    Finds the CSV files in our directory
'''

from os import listdir
from os.path import isfile, join

def findFiles(path):
    # first find the files in the directory
    dirfiles = [f for f in listdir(path) if isfile(join(path, f)) and f.endswith('.csv')]

    CSVFiles = {}

    # get the subscriptions csv
    CSVFiles['subscriptions'] = path + [x for x in dirfiles if x.startswith('cratejoy_Subscriptions')][0]

    # get the transactions csv
    CSVFiles['transactions'] = path + [x for x in dirfiles if x.startswith('cratejoy_Transactions')][0]

    # get the orders csv
    CSVFiles['orders'] = path + [x for x in dirfiles if x.startswith('cratejoy_Orders')][0]

    return CSVFiles