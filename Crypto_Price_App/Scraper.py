import bs4
import locale
from urllib.request import urlopen as urlO
from twython import Twython
from bs4 import BeautifulSoup
from apscheduler.schedulers.blocking import BlockingScheduler
import datetime
import time
import array

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
#twitter.update_status(status="@ohioboy2 Started This Tweet Stream for #ETH " + initdate_time + ".. updating every 2 minutes.")
print('Initializing Time: ' + initdate_time)

cryptoindex = 1

def get_crypto_price():
    uClient = urlO(my_url)
    page_html = uClient.read()
    uClient.close()
    # turn into beautiful soup
    page_soup = BeautifulSoup(page_html, "html.parser")
    price = page_soup.findAll("a", {"class": "price"})
    return price[cryptoindex];
    # print("$"+containers[0].strong.text + containers[0].sup.text)

# Set initial value to compare initial public price pull.
last_value = get_crypto_price().text

lastvalues = array.array('f', [])

# Get current time stamp


def get_timestamp():
    starttime = time.time()
    startdate_time = datetime.datetime.fromtimestamp(starttime).strftime('%Y-%m-%d %H:%M:%S')
    return startdate_time;


def get_value_change(last_value, current_price):
    current_price.strip()
    current_price = current_price.replace('$', '')
    last_value.strip()
    last_value = last_value.replace('$', '')
    change = float(current_price) - float(last_value)
    pchange = change/float(last_value)
    # print(round(change,3))
    last_value = current_price
    return pchange * 100


def get_crypto_name():
    client = urlO(my_url)
    page_html = client.read()
    client.close()
    # turn into beautiful soup
    page_soup = BeautifulSoup(page_html, "html.parser")
    crypto = page_soup.findAll("td", {"class": "no-wrap currency-name"})
    return crypto[cryptoindex];

# Add values to an array

def add_value(value):
    value.strip()
    value = value.replace('$', '')
    lastvalues.append(float(value))
    print(lastvalues[len(lastvalues)-1])
    return

# Print array values

def print_values():
    k = 0
    while k < len(lastvalues):
        print(lastvalues[k])
        k += 1

# Check if should tweet a price change alert

def should_tweet(lvalue, cvalue):
    value_changed = get_value_change(lvalue, cvalue)
    if abs(value_changed) >= 0.002:
        print("!!! ALERT: Price has changed by: " + str(round(value_changed, 6)) + "% !!!")

# Schedule The Task

def some_job():
    # got info from page
    startdate_time = get_timestamp()
    print('Started pull at: ' + startdate_time)
    print_values()
    # set lowest price as first index item

    lowest_price = get_crypto_price().text
    add_value(lowest_price)
    change_in_price = get_value_change(last_value, lowest_price)
    should_tweet(last_value, lowest_price)
    outputtext = 'Time Stamp of Last Price of Etherum ' + get_timestamp() + ' ' + lowest_price.strip() + \
                 " with a change of " + str(round(change_in_price, 6)) + '%'
    #twitter.update_status(status=outputtext)
    print(outputtext)

# run scheduler
scheduler = BlockingScheduler()
scheduler.add_job(some_job, 'interval', minutes=5)
scheduler.start()
