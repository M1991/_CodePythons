
import csv
from bs4 import BeautifulSoup
import requests 


######### Collects all the data, ID, TAGS, Classes without any filters
# URL = "https://www.geeksforgeeks.org/data-structures/"
# r = requests.get(URL) 
# print(r.content) 



# page = requests.get('https://web.archive.org/web/20121007172955/http://www.nga.gov/collection/anZ1.htm')
page = requests.get('https://www.geeksforgeeks.org/data-structures/')

soup = BeautifulSoup(page.text, 'html.parser')

last_links = soup.find(class_='entry-content')
# last_links.decompose()

# Create a file to write to, add headers row
f = csv.writer(open('Test_names.csv', 'w'))
f.writerow(['Name', 'Link'])

artist_name_list = soup.find(class_='entry-content')
artist_name_list_items = artist_name_list.find_all('entry-content')

for artist_name in artist_name_list_items:
    names = artist_name.contents[0]
    links = 'https://www.geeksforgeeks.org/data-structures/' # + artist_name.get('href')


    # Add each artist’s name and associated link to a row
    f.writerow([names, links])