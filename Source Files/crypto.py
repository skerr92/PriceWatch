import bs4
import locale
from urllib import urlopen as urlO
from bs4 import BeautifulSoup
#from sys import argv

locale.setlocale( locale.LC_ALL, 'en_US.UTF-8' )

# Reference URL
my_url = 'https://coinmarketcap.com/all/views/all/'

#got info from page
uClient = urlO(my_url)
page_html= uClient.read()
uClient.close()

#turn into beautiful soup
page_soup = BeautifulSoup(page_html, "html.parser")
crypto = page_soup.findAll("td", {"class":"text-left col-symbol"})
price = page_soup.findAll("td", {"class":"no-wrap text-right"})
#print("$"+containers[0].strong.text + containers[0].sup.text)

#set lowest price as first index item
lowest_price = price[0].text
print('Bitcoin Price: '+crypto[0].text+lowest_price)