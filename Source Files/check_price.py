# Author: Seth Kerr
# Created: 11-01-2018
# Contributors: Add Contributors here
#
# Purpose of this file is to integrate the Google Search API python library to generate custom search based for particular items
# like a Nintendo Switch
#
# Start Code after this line
#

from textblob import TextBlob
import requests
#from requests import urlopen as urlO
from bs4 import BeautifulSoup
from sys import argv


class Analysis:
	def __init__(self, term):
		self.term = term
		self.num_products = 0
		#self.subjectivity = 0
		#self.sentiment = 0

		self.url = 'https://www.google.com/search?q={0}&source=lnms&tbm=shop'.format(self.term)

	def run (self):
		response = requests.get(self.url)
		soup = BeautifulSoup(response.text, 'html.parser')
		product_results = soup.find_all('div', class_='sh-dlr__list-result')
		for p in product_results:
			self.num_products += 1


a = Analysis(argv[1])
a.run()
print(a.term, 'Number of Products', a.num_products)

