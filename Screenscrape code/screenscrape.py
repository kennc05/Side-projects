# import libraries
#ONLY WORKS ON PYTHON 2.7!!!!!!

#sources:http://docs.python-requests.org/en/master/user/quickstart/#make-a-request
#sources:https://medium.freecodecamp.org/how-to-scrape-websites-with-python-and-beautifulsoup-5946935d93fe
#sources:https://stackoverflow.com/questions/2953746/python-parse-comma-separated-number-into-int
#sources:https://stackoverflow.com/questions/42057086/scraping-php-site-with-python-for-a-beginner
#built with sweat and tears by Kenneth btw


import requests
from bs4 import BeautifulSoup

# specify the url
URL = 'http://www.marketaxess.com/trading/sef-data.php'
page = requests.get(URL)
print ('Fetching URL '+URL)
print ('Status code of page fetch: '+str(page.status_code))
soup = BeautifulSoup(page.content, 'html.parser')

result= soup.find_all('td', class_='')
list = [pt.get_text() for pt in result]

price1=list[0]
price2=list[5]

try:
    price3=list[10]
except IndexError:
    price3= '0'


print('Calculating....')
print('Price1: $'+price1+' | Price2: $'+price2+' | Price3: $'+price3)
result=int(price1.replace(',',''))+int(price2.replace(',',''))+int(price3.replace(',',''))


print('The total price is $'+str(result))
