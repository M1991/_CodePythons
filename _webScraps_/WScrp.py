### Try install the followig libraries 
### pip install requests
### pip install html5lib
### pip install bs4 
###

import requests 
from bs4 import BeautifulSoup 
import csv 
  
# URL = "http://www.values.com"
URL = "https://www.geeksforgeeks.org"

r = requests.get(URL) 
  
soup = BeautifulSoup(r.content, 'html5lib') 
  
quotes=[]  # a list to store quotes 
  
table = soup.find('div', attrs = {'id':'container'}) 
  
for row in table.findAll('div', attrs = {'class':'quote'}): 
    quote = {} 
    quote['theme'] = row.h5.text 
    quote['url'] = row.a['href'] 
    quote['img'] = row.img['src'] 
    quote['lines'] = row.h6.text 
    quote['author'] = row.p.text 
    quotes.append(quote) 
  
filename = 'Testing_codes.csv'
with open(filename, 'wb') as f: 
    w = csv.DictWriter(f,['theme','url','img','lines','author']) 
    w.writeheader() 
    for quote in quotes: 
        w.writerow(quote) 