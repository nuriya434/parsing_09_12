import requests
import json
from bs4 import BeautifulSoup

url="https://quotes.toscrape.com/"

responce=requests.get(url)
# print(responce.text)

soup = BeautifulSoup(responce.text, 'lxml')
# print(soup)
qoutes = soup.find_all('span', class_='text')
authors=soup.find_all("small", class_='author')

data = {}

for i in range(len(qoutes)):
    print(f"{authors[i].text}: {qoutes[i].text}")
    data[authors[i].text]=qoutes[i].text
print(data)
with open("data.json", 'w', encoding='utf-8') as fp:
    json.dump(data, fp)

    
# for quote in qoutes:
#     print(quote.text)

# for author in authors:
#     print(author.text)

# print(qoutes)