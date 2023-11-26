from bs4 import BeautifulSoup
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

def get_number_from_string(string):
    return float(''.join([x for x in string if x.isdigit() or x == '.']))
def gold_price():
    
    d=requests.get(url='https://economictimes.indiatimes.com/commoditysummary/symbol-GOLD.cms')
    soup=BeautifulSoup(d.text,'html.parser')
    p=soup.find('li',class_="commodityPriceCol").find('span',class_="commodityPrice")
    
    return int(float(p.text))
def silver_price():
    d=requests.get(url='https://economictimes.indiatimes.com/commoditysummary/symbol-SILVER.cms')
    soup=BeautifulSoup(d.text,'html.parser')
    p=soup.find('li',class_="commodityPriceCol").find('span',class_="commodityPrice")
          
    
    return int(float(p.text)*0.01)
#print(gold_price())


