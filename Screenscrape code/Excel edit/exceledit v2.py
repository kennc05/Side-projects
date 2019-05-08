#https://stackoverflow.com/questions/44265975/remove-last-number-of-a-integer
#https://stackoverflow.com/questions/16823695/how-to-use-delimiter-for-csv-in-python
#https://stackoverflow.com/questions/45978295/saving-a-downloaded-csv-file-using-python?rq=1
#https://stackoverflow.com/questions/26957831/edit-existing-excel-workbooks-and-sheets-with-xlrd-and-xlwt
#https://stackoverflow.com/questions/3348460/csv-file-written-with-python-has-blank-lines-between-each-row

#import the libraries needed to run the program
import csv #allows python to read and write data in a csv format
import requests #allows python to grab a file from a website 

#defining where the CSV URL will be 
CSV_URL = 'http://www3.icap.com/sef/marketdata/igdl/ICAPSEFMarketDataIGDL.csv'

#starting the downlaod session to grab the file
with requests.Session() as s:
    download = s.get(CSV_URL)

    #decoding the file from utf-8 for python to be able to read from     
    decoded_content = download.content.decode('utf-8')

    #using the .reader function that allows the program to distinguish between
    #seperate characters when there is the '|' delimiter
    csv_file = csv.reader(decoded_content.splitlines(), quotechar =',', delimiter='|')

    #creates a new list where all rows are stored in
    csv_list = list(csv_file)

    #creates a new csv file called out.csv and the variable for it is known as file
    with open('out.csv', 'w', newline='') as file:
        #defining a writer variable where it writes to the csv file
        writer = csv.writer(file)
        #defining total which will hold the value for the grand total
        total = 0

        #calculating the total amount in the last column of the spreadsheet (column Z)
        for row in csv_list:
                try:
                    #row[25] is also known as column Z on a spreadsheet    
                    total = total + int(row[25])
                 #when there is a value error such as the value not being a number, it defaults to 0 for that row   
                except ValueError:
                    total = 0
                    
        #creating a new row to be appended to the spreadsheet
        resultsrow = []

        #creating a new variable to add blank spaces so that the total can be added to the corret column (column Z)
        blankspaces=0
        while blankspaces!=24:
                #adding white spaces 24 times (columns A-X)
                resultsrow.append('')
                blankspaces=blankspaces+1

        #new total removes the last 3 digits from the result
        newtotal = total // 1000

        #add ICAP IRS to column X and the new total to column Z
        resultsrow.append('ICAP IRS')
        resultsrow.append(str(newtotal))
        csv_list.append(resultsrow)

        #now added every row in the list csv_list to the spreadsheet itself        
        for row in csv_list:
                writer.writerow(row)

        #printing out the results 
        print('The Total Notional USD NDA is '+str(total))
        print('Without the last 3 digits, the ICAP IRS is '+str(newtotal))
        print('Please find the generated spreadsheet within the folder')
        


