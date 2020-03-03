import requests
from bs4 import BeautifulSoup

url = "https://dhhumanist.org"
result = requests.get("https://dhhumanist.org/")

print(result.status_code)
print(result.headers)
page = result.content

# How would we get all the links to volumes from the Humanist Page?

soup = BeautifulSoup(page)
rows = soup.find_all('td')


for row in rows:
    link = row.find('a').get('href')
    print(url+link, row.text)
    if 'Archive' in link:
        volume_result = requests.get(url+link)
        volume_page = volume_result.content
        # print(volume_page)
        volume_soup = BeautifulSoup(volume_page, 'html.parser')
        volume_links = volume_soup.find_all('a')
        # print(volume_links)
        for l in volume_links:
            if 'txt' in l:
                print(l.get('href'))


# How would we get all the text from each volume and save it to a csv?