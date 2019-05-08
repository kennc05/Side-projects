# import libraries
#ONLY WORKS ON PYTHON 2.7!!!!!!

#sources:http://docs.python-requests.org/en/master/user/quickstart/#make-a-request
#sources:https://medium.freecodecamp.org/how-to-scrape-websites-with-python-and-beautifulsoup-5946935d93fe
#sources:https://stackoverflow.com/questions/2953746/python-parse-comma-separated-number-into-int
#sources:https://stackoverflow.com/questions/42057086/scraping-php-site-with-python-for-a-beginner
#built with sweat and tears by Kenneth btw

#import the libraries used to load the website and get the html code of the site
import requests
from bs4 import BeautifulSoup

# specify the url to go to which is the market one
URL = 'http://www.marketaxess.com/trading/sef-data.php'
page = requests.get(URL) #load the URL
print ('Fetching data from URL '+URL)
print ('Status code of page fetch: '+str(page.status_code))

#Makes the HTML python friendly with soup
soup = BeautifulSoup(page.content, 'html.parser')


#get the instrument names and put them into a list
result= soup.find_all('td', class_='instrument')
instruments = [pt.get_text() for pt in result]

instrumentcount=0
for pt in result:
    instrumentcount=instrumentcount+1

instrument1=instruments[0]
instrument2=instruments[1]

#If the 3rd instrument is not present, then it will be called none found or N/A
try:
    instrument3=instruments[2]
    instrument4=instruments[3]
    instrument5=instruments[4]
except IndexError:
    instrument3='N/A'
    instrument4='N/A'
    instrument5='N/A'
    
#get all of the instrument prices
result= soup.find_all('td', class_='')
prices = [pt.get_text() for pt in result]

price1=prices[0]
price2=prices[5]

#Again, if the third instrument is not found, the price defaults to 0
try:
    price3=prices[10]
    price4=prices[15]
    price5=prices[20]
except IndexError:
    price3='0'
    price4='0'
    price5='0'

#Print the output of results + calculate end result
print('Calculating....')
print('')
print('Found '+str(instrumentcount)+' instruments:')



print(instrument1+' : $'+price1)

if instrumentcount==2:
    print(instrument2+' : $'+price2)
if instrumentcount==3:
    print(instrument3+' : $'+price3)
if instrumentcount==4:
    print(instrument4+' : $'+price4)
if instrumentcount==5:
    print(instrument5+' : $'+price5)
            
    
result=int(price1.replace(',',''))+int(price2.replace(',',''))+int(price3.replace(',',''))

print('')
print('The total price is $'+str(result))
