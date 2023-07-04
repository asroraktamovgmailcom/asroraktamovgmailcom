import requests
from pprint import pprint
url = 'https://bbc.com/news'
respons = requests.get(url)
pprint(respons.text[:1000])