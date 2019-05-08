import requests
import csv

spreadsheetlocation = 'http://www3.icap.com/sef/marketdata/igdl/ICAPSEFMarketDataIGDL.csv'
getspreadsheet = requests.get(spreadsheetlocation)

file = open('out.csv', 'wb')

with open('out.csv', 'wb') as f:
    writer = csv.writer(file, delimiter ='|')
    reader = csv.reader(file)
    
    for row in reader:
        writer.writerow(row)


