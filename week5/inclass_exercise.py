import requests
from bs4 import BeautifulSoup

# Example of using Requests https://gist.github.com/bradmontgomery/1872970
url = "https://dhhumanist.org"
result = requests.get(url)

# print(result.status_code)
# print(result.headers)
page = result.content


soup = BeautifulSoup(page, features="lxml")

links = soup.find_all('a')

for link in links:
    if 'Archive' in link.get('href'):
        print(url + link.get('href'))
        volume_page = requests.get(url + link.get('href'))
        volume_soup = BeautifulSoup(volume_page.content, features='lxml')
        volume_links = volume_soup.find_all('a')
        print(volume_links)
        
# print(soup.prettify())
# How would we get all the links to volumes from the Humanist Page?

# How would we get all the text from each volume and save it to a csv?