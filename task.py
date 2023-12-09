import requests
import json
from bs4 import BeautifulSoup

url="https://scrapingclub.com/"

responce=requests.get(url)
soup = BeautifulSoup(responce.text, 'lxml')

numbers = soup.find_all('div',class_="py-2 bg-gray-50 border-b")
titles=soup.find_all("h4", class_='card-title')
descrips=soup.find_all("p", class_="card-text")

data = []

for i in range(len(numbers)):
    dict={}
    if 'ajax' in titles[i].text.lower():
        dict['numbers']=numbers[i].text
        dict['titles']=titles[i].text
        dict['descrips']=descrips[i].text
        data.append(dict)
    
with open("data_2.json", 'w', encoding='utf-8') as fp:
    json.dump(data, fp)

    
# for quote in qoutes:
#     print(quote.text)

# for author in authors:
#     print(author.text)

# print(qoutes)