import bs4
import locale
from urllib.request import urlopen as urlO
from twython import Twython
from bs4 import BeautifulSoup
from apscheduler.schedulers.blocking import BlockingScheduler
import datetime
import time

locale.setlocale( locale.LC_ALL, 'en_US.UTF-8' )

# keys/secrets as strings in the following fields
credentials = {}
APP_KEY = ""
APP_SECRET = ""
ACCESS_TOKEN = ""
ACCESS_SECRET = ""


# Instantiate an object
twitter = Twython(APP_KEY, APP_SECRET, ACCESS_TOKEN, ACCESS_SECRET)
twitter.verify_credentials()
twitter.get_home_timeline()

# Reference URL
my_url = 'https://coinmarketcap.com/'
inittime = time.time()
initdate_time = datetime.datetime.fromtimestamp(inittime).strftime('%Y-%m-%d %H:%M:%S')
twitter.update_status(status="Seth Started This Tweet Stream for #BTC " + initdate_time + ".. updating every 5 minutes.")
print('Initializing Time: ' + initdate_time)


def get_crypto_price():
    uClient = urlO(my_url)
    page_html = uClient.read()
    uClient.close()
    # turn into beautiful soup
    page_soup = BeautifulSoup(page_html, "html.parser")
    crypto = page_soup.findAll("td", {"class": "no-wrap currency-name"})
    price = page_soup.findAll("td", {"class": "no-wrap text-right"})
    return price[0];
    # print("$"+containers[0].strong.text + containers[0].sup.text)

#Get current time stamp

def get_timestamp():
    starttime = time.time()
    startdate_time = datetime.datetime.fromtimestamp(starttime).strftime('%Y-%m-%d %H:%M:%S')
    return startdate_time;

#Schedule The Task
def some_job():
    # got info from page
    startdate_time = get_timestamp()

    print('Started pull at: ' + startdate_time)

    #set lowest price as first index item
    lowest_price = get_crypto_price().text
    outputtext = 'Time Stamp of Last Price of #BTC ' + get_timestamp() + lowest_price
    twitter.update_status(status=outputtext)
    print(outputtext)

# run scheduler


scheduler = BlockingScheduler()
scheduler.add_job(some_job, 'interval', minutes=5)
scheduler.start()
