
# https://www.youtube.com/watch?v=0_VZ7NpVw1Y
# https://www.youtube.com/watch?v=XQgXKtPSzUI  -- Trying from this video

import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

myurl = 'https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphics%20cards'

## Open up the connection and download the web page
uClinet = uReq(myurl)
page_Html = uClinet.read()
uClinet.close()


## HTML parser
# page_soup = soup(page_Html, "html.parser")
page_soup = soup(page_Html, "html.parser")

## print(page_soup.h1)

## Grabs each products
html_container = page_soup.findAll("div", {"class":"item-container"})  # {} - object

# contn = html_container[0] # gets the content in item-container

for container in html_container:
   # brand = container.div.div.a.img["title"]
    
    title_Name =  container.findAll("a", {'class': 'item-title'})
    prd_name = title_Name[0].text 

    _container = container.findAll("li", {'class':'price-ship'})
    shp_container = _container[0].text.strip()

    # print(brand)
    print("\n", prd_name)
    print("\n", shp_container)

## Writing into CSV

filename = "products.csv"  # check  for changing the file name
f =open(filename, "w")
headers = "brand, product_name, shipping \n"
f.write(headers)

## Save to default location 
f.write(prd_name +""+ shp_container.replace(",","|") +"\n")
f.close()