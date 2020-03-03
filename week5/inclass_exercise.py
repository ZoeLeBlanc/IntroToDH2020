import requests
from bs4 import BeautifulSoup

# Example of using Requests https://gist.github.com/bradmontgomery/1872970

result = requests.get("https://dhhumanist.org/")

print(result.status_code)
print(result.headers)
page = result.content


soup = BeautifulSoup(page)
print(soup.prettify())
# How would we get all the links to volumes from the Humanist Page?

# How would we get all the text from each volume and save it to a csv?