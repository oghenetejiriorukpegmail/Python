from bs4 import BeautifulSoup
import requests
from pprint import pprint

url = 'https://web.telegram.org/?legacy=1#/im?p=c1518994770_4201945232006510029'

resp = requests.get(url)
print (resp.headers)
print (resp.text)