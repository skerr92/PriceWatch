import bs4
import locale
from urllib.request import urlopen as urlO
from bs4 import BeautifulSoup
from apscheduler.schedulers.blocking import BlockingScheduler
import datetime
import time

locale.setlocale( locale.LC_ALL, 'en_US.UTF-8' )

# Reference URL
my_url = 'https://coinmarketcap.com/'
inittime = time.time()
initdate_time = datetime.datetime.fromtimestamp(inittime).strftime('%Y-%m-%d %H:%M:%S')
print('Initializing Time: ' + initdate_time)

# Creating scheduling task

def some_job():
    # got info from page
    starttime = time.time()
    startdate_time = datetime.datetime.fromtimestamp(starttime).strftime('%Y-%m-%d %H:%M:%S')

    print('Started pull at: ' + startdate_time)

    uClient = urlO(my_url)
    page_html= uClient.read()
    uClient.close()
    # turn into beautiful soup
    page_soup = BeautifulSoup(page_html, "html.parser")
    crypto = page_soup.findAll("td", {"class":"no-wrap currency-name"})
    price = page_soup.findAll("td", {"class":"no-wrap text-right"})
    # print("$"+containers[0].strong.text + containers[0].sup.text)

    ts = time.time()
    date_time = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

    #set lowest price as first index item
    lowest_price = price[0].text
    outputtext = 'Time Stamp of Last Price of ' + crypto[0].text + date_time + lowest_price
    print(outputtext)

# run scheduler


scheduler = BlockingScheduler()
scheduler.add_job(some_job, 'interval', minutes=.25)
scheduler.start()

