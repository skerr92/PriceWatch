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
from bs4 import BeautifulSoup
from sys import argv


class Analysis:
	def __init__(self, term):
		self.term = term
		self.price = 0


		self.url = 'https://www.google.com/search?q={0}&source=lnms&tbm=nws'.format(self.term)

	def run (self):
		response = requests.get(self.url)
		soup = BeautifulSoup(response.text, 'html.parser')
		headline_results = soup.find_all('div', class_='st')
		for h in headline_results:
			blob = TextBlob(h.get_text())
			self.sentiment += blob.sentiment.polarity / len(headline_results)
			self.subjectivity += blob.sentiment.subjectivity / len(headline_results)


a = Analysis(argv[1])
a.run()
print(a.term, 'Subjectivity: ', a.subjectivity, 'Sentiment: ', a.sentiment)