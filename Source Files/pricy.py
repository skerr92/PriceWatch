# This is for testing out code that is said to work via this youtube video 
#
# URL: https://www.youtube.com/watch?v=XQgXKtPSzUI
#
# Not sure if it will actually work, but we will see
#
# Start code after this line:

import bs4
import locale
from urllib import urlopen as urlO
from bs4 import BeautifulSoup
from sys import argv

locale.setlocale( locale.LC_ALL, 'en_US.UTF-8' )

# Reference URL
my_url = 'https://www.newegg.com/Product/ProductList.aspx?Submit=ENE&N=100006740%2050010418&IsNodeId=1&cm_sp=Cat_Laptops-_-PopBrands-_-Lenovo_3'

#got info from page
uClient = urlO(my_url)
page_html= uClient.read()
uClient.close()

#turn into beautiful soup
page_soup = BeautifulSoup(page_html, "html.parser")
containers = page_soup.findAll("li", {"class":"price-current"})
description = page_soup.findAll("a", {"class":"item-title"})
#print("$"+containers[0].strong.text + containers[0].sup.text)

#set lowest price as first index item
lowest_price = locale.atof(containers[0].strong.text + containers[0].sup.text)
print('Before Sort Lowest Price: \n'+description[0].text+'\n'+'$'+str(lowest_price))

#compare all prices to find and set the actual lowest price
index = 0
lowest_price_index = 0
max_index = len(containers)
while (index < max_index):
	current_price = locale.atof(containers[index].strong.text + containers[index].sup.text)
	if (current_price < lowest_price):
		lowest_price = current_price
		lowest_price_index = index
	index += 1

#print the lowest price
print(description[lowest_price_index].text+'\nActual Lowest Price: $'+str(lowest_price))

