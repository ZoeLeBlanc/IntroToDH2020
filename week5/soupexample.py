from bs4 import BeautifulSoup
import csv

soup = BeautifulSoup(open("43rd-congress.html"), features="lxml")
# print(soup.prettify())

# f = csv.writer(open("43rd_Congress.csv", "w"))
# f.writerow(["Name", "Link"])    # Write column headers as the first line
divs = soup.find_all('div', class_="row memberWhite")
# print(divs)
for div in divs:
    print(div.find('a').get('href'))
    link = div.contents[1].find("a").get("href")
    names = div.contents[1].find("a").text
    # print(link, names)
#     names = link.contents[0]
#     print(names)
    # fullLink = link.get('href')
    # print(names, fullLink)
    # f.writerow([names,fullLink])

# links = soup.find_all('a', class_="red")
# for link in links:
#     names = link.contents
#     fullLink = link.get('href')
#     print(names)
#     print(fullLink)