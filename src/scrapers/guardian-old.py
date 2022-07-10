from requests_html import HTMLSession
from bs4 import BeautifulSoup
import pandas as pd

# sample = 'https://www.theguardian.com/world/ukraine?page=255'
term = 'ukraine'
s = HTMLSession()


def getdata(term, page):
    url = f'https://www.theguardian.com/world/{term}?page={page}'
    r = s.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    return soup


def convert(soup):
    sections = soup.find_all('div', {'class': 'fc-container__inner'})
    for section in sections:
        date = section.find('time', {'class': 'fc-date-headline'}).text.strip()
        container = section.find_all('div', {'class': 'fc-item__container'})
        for item in container:
            heading = item.find('a', {'class': 'u-faux-block-link__overlay'}).text.strip()
            timestamp = item.find('span', {'class': 'fc-timestamp__text'}).text.strip().replace('Published: ', '')
            link = item.find('a', {'class': 'u-faux-block-link__overlay'})['href']
            try:
                image = item.find('img', {'class': 'responsive-img'})['src']
            except:
                image = ''
            data = {
                'date': date,
                'timestamp': timestamp,
                'heading': heading,
                'url': link,
                'image': image
            }
            articlesarray.append(data)
    return


articlesarray = []

for page in range(0, 250, 1):
    soup = getdata(term, page)
    print(page)
    convert(soup)


df = pd.DataFrame(articlesarray)
print(df.head())
df.to_csv('guardian-war-ukraine-query.csv')
df.to_json('guardian-war-ukraine-query.json')
print(len(articlesarray))
