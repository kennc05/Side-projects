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
result= soup.find_all('td', class_='')
prices = [pt.get_text() for pt in result]


print (prices[5])

