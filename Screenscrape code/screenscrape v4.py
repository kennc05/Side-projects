# import libraries

#sources:http://docs.python-requests.org/en/master/user/quickstart/#make-a-request
#sources:https://medium.freecodecamp.org/how-to-scrape-websites-with-python-and-beautifulsoup-5946935d93fe
#sources:https://stackoverflow.com/questions/2953746/python-parse-comma-separated-number-into-int
#sources:https://stackoverflow.com/questions/42057086/scraping-php-site-with-python-for-a-beginner
#sources: https://www.geeksforgeeks.org/writing-excel-sheet-using-python/
#sources: https://pypi.org/project/xlwt/
#sources: https://buxty.com/b/2011/10/widths-heights-with-xlwt-python/
#import: requests, xlwt, bs4 | pip install <libraryname>

#import the libraries used to load the website and get the html code of the site
#https://stackoverflow.com/questions/4010840/generating-variable-names-on-fly-in-python


import requests #allows you to load a website via python
from bs4 import BeautifulSoup #makes html code python friendly

# specify the url to go to which is the market one
URL = 'http://www.marketaxess.com/trading/sef-data.php'
page = requests.get(URL) #load the URL
print ('Fetching data from URL '+URL)
print ('Status code of page fetch: '+str(page.status_code)) #https://www.restapitutorial.com/httpstatuscodes.html


#Makes the HTML python friendly with soup
soup = BeautifulSoup(page.content, 'html.parser')


#get the instrument names and put them into a list
#soup.find_all('<tag>', class_='classname')
result= soup.find_all('td', class_='instrument')
#retrieves the text from website within the instruments column, and assigns the text to the variable "instruments"
instruments = [pt.get_text() for pt in result]

instrumentcount = 0

for pt in result:
    instrumentcount=instrumentcount+1


#get all of the instrument volumes
result= soup.find_all('td', class_='')
volumes = [pt.get_text() for pt in result]

print('')
print("Instrument = Total Volume USD ('000)")

volumetotal=0
for i in range (instrumentcount):
    vars()[instruments[0]]=volumes[0]
    volumetotal=volumetotal+int(volumes[i*5].replace(',',''))
    print (instruments[i] + ' = $' + volumes[i*5])


print('')
print("The Total Volume USD ('000) is $"+format (volumetotal, ',d')) #add a comma to the result.... e.g $61000 > $61,000



# Writing to an excel using the xlwt library  
# sheet using Python 
import xlwt 
from xlwt import Workbook #allows you to create and write to a workbook in excel
  
# Workbook is created - Workbook() creates a new workbook
wb = Workbook() 

# add_sheet is used to create sheet. 
sheet = wb.add_sheet('Sheet 1')

first_col = sheet.col(0) #Also known as Column A
first_col.width = 256 * 20 #Increase width to 20 Characters long

#Writes to the new sheet that was created
#sheet.write(Vertical coordinate, Horizontal coordinate, 'Value to be put in')
sheet.write(0, 0, 'Instrument name') #Outputs "Instrument name" in A1
sheet.write(0, 1, "Total Volume USD ('000)")

for i in range (instrumentcount):
    vars()[instruments[0]]=volumes[0]
    sheet.write(1+i, 0, instruments[i])
    sheet.write(1+i, 1, volumes[i*5])

sheet.write(instrumentcount+2, 0, 'Market Axess CDS')
sheet.write(instrumentcount+2, 1, format (volumetotal, ',d'))

print('Saving results to excel spreadsheet...')
wb.save('volumes.xls') #Saves the workbook as volumes.xls - overwrites the existing file
print('Successfully saved! Please check the folder')
