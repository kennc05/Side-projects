# import libraries
#ONLY WORKS ON PYTHON 2.7!!!!!!

#sources:http://docs.python-requests.org/en/master/user/quickstart/#make-a-request
#sources:https://medium.freecodecamp.org/how-to-scrape-websites-with-python-and-beautifulsoup-5946935d93fe
#sources:https://stackoverflow.com/questions/2953746/python-parse-comma-separated-number-into-int
#sources:https://stackoverflow.com/questions/42057086/scraping-php-site-with-python-for-a-beginner
#sources: https://www.geeksforgeeks.org/writing-excel-sheet-using-python/
#sources: https://pypi.org/project/xlwt/
#sources: https://buxty.com/b/2011/10/widths-heights-with-xlwt-python/

#built with sweat and tears by Kenneth btw

#import the libraries used to load the website and get the html code of the site
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

instrumentcount=0
#counts how many instruments there are and repeats until all instruments are found  
for pt in result:
    instrumentcount=instrumentcount+1

instrument1=instruments[0]
instrument2=instruments[1]

#If the 3rd instrument is not present, then it will be called none found or N/A. Have added this section, just to cater for more instruments being added to the website. Therefore this code will not be edited and will still output all the instruments displayed. 
try:
    instrument3=instruments[2]
    instrument4=instruments[3]
    instrument5=instruments[4]
except IndexError:
    instrument3='N/A'
    instrument4='N/A'
    instrument5='N/A'
# if instrument 3/4/5 do not exist, then no values will be printed and only instruments found will be present
#get all of the instrument volumes
result= soup.find_all('td', class_='')
volume = [pt.get_text() for pt in result]

volume1=volume[0]
volume2=volume[5]

#Again, if the third instrument is not found, the volume defaults to 0
try:
    volume3=volume[10]
    volume4=volume[15]
    volume5=volume[20]
except IndexError:
    volume3='0'
    volume4='0'
    volume5='0'
# if volumes 3/4/5 do not exist, then no values will be printed and only volumes found will be present

#Print the output of results + calculate end result
print('Calculating....')
print('')
print('Found '+str(instrumentcount)+' instruments:')


#print out all of the volumes if found
print(instrument1+' : $'+volume1)

if instrumentcount==2:
    print(instrument2+' : $'+volume2)
if instrumentcount==3:
    print(instrument3+' : $'+volume3)
if instrumentcount==4:
    print(instrument4+' : $'+volume4)
if instrumentcount==5:
    print(instrument5+' : $'+volume5)
            
#Removing the ',' with a '' so that the number becomes an interger. E.G 25,000 to 25000. 
result=int(volume1.replace(',',''))+int(volume2.replace(',',''))+int(volume3.replace(',',''))+int(volume4.replace(',',''))+int(volume5.replace(',',''))

print('')
print("The Total Volume USD ('000) is $"+format (result, ',d')) #add a comma to the result.... e.g $61000 > $61,000




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
sheet.write(1, 0, instrument1) #A2

if instrumentcount==2:
    sheet.write(2, 0, instrument2)

if instrumentcount==3:
    sheet.write(3, 0, instrument3)

if instrumentcount==4:
    sheet.write(4, 0, instrument4)

if instrumentcount==5:
    sheet.write(5, 0, instrument5)

    
second_col = sheet.col(1) #Column B 
second_col.width = 256 * 25 #Increase width to 20 characters long

sheet.write(0, 1, "Total Volume USD ('000)")
sheet.write(1, 1, volume1)

if instrumentcount==2:
    sheet.write(2, 1, volume2)

if instrumentcount==3:
    sheet.write(3, 1, volume3)

if instrumentcount==4:
    sheet.write(4, 1, volume4)

if instrumentcount==5:
    sheet.write(5, 1, volume5)


sheet.write(6, 0, 'Market Axess CDS')
sheet.write(6, 1, format (result, ',d'))

print('Saving results to excel spreadsheet...')
wb.save('volumes.xls') #Saves the workbook as volumes.xls - overwrites the existing file
print('Successfully saved! Please check the folder')
