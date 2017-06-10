import requests
from lxml import html
import re
import urllib
import urls
import datetime

def scrape_latest_price(url, fuel_type, city):
    try:
        request = urllib.request.Request(url)
        response = urllib.request.urlopen(request)
        r = requests.get(url)
        data = r.content
        tree = html.fromstring(data)
        recent_price_complete = tree.xpath('//span[@class="price"]/text()')
        recent_price = recent_price_complete[0].split('=')[1].split('Rs')[0].replace(' ','')
        ts = datetime.datetime.now().strftime("%A, %d. %B %Y %I:%M%p")
        if re.match("^\d+?\.\d+?$", recent_price) is None:
            print (ts,'\t')
            print ("[ERROR] Invalid ",fuel_type,"Price retrieved for",city)
            return -1
    
        return float(recent_price)

    except urllib.error.HTTPError as err:
        ts = datetime.datetime.now().strftime("%A, %d. %B %Y %I:%M%p")
        print (ts,'\t[ERROR] Invalid URL for',fuel_type,'prices in',city) 
        return -1   

def scrape_all_diesel_prices():
    url_dict = urls.diesel_urls()
    diesel_prices = {}
    
    for city in url_dict:
        scraped_price = scrape_latest_price(url_dict[city], "Diesel", city)
        if scraped_price > 0.0:
            diesel_prices[(city).title()] = scraped_price
    return diesel_prices

def scrape_all_petrol_prices():
    url_dict = urls.petrol_urls()
    petrol_prices = {}
    
    for city in url_dict:
        scraped_price = scrape_latest_price(url_dict[city], "Petrol", city)
        if scraped_price > 0.0:
            petrol_prices[(city).title()] = scraped_price     
    
    return petrol_prices
