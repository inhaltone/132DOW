from requests_html import HTMLSession
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.theguardian.com/world/ukraine/2022/feb/23/all'
s = HTMLSession()


def getdata(url):
    r = s.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    return soup


def getnextpage(link):
    page = link.find('div', {'class': 'pagination u-cf'})
    if not page.find('a', {'class': 'pagination__action--pushleft'}):
        return
    else:
        url = page.find('a', {'class': 'pagination__action--pushleft'})['href']
        return url


def transform(soup: object) -> object:
    articles = soup.find_all('div', {'class': 'fc-item__container'})
    day = soup.find('span', {'class': 'fc-today__dayofweek'}).text.strip()
    daymonth = soup.find('span', {'class': 'fc-today__dayofmonth'}).text.strip()
    month = soup.find('span', {'class': 'fc-today__month'}).text.strip()
    year = soup.find('span', {'class': 'fc-today__year'}).text.strip()
    date = f'{day}, {daymonth} {month} {year}'
    for article in articles:
        heading = article.find('a', {'class': 'u-faux-block-link__overlay'}).text.strip()
        link = article.find('a', {'class': 'u-faux-block-link__overlay'})['href']
        try:
            image = article.find('img', {'class': 'responsive-img'})['src']
        except:
            image = ''

        data = {
            'date': date,
            'heading': heading,
            'link': link,
            'image': image
        }
        articlesList.append(data)
    return


articlesList = []

while True:
    soup = getdata(url)
    url = getnextpage(soup)
    transform(soup)
    if not url:
        break
    print(url)

df = pd.DataFrame(articlesList)
print(df.head())
df.to_csv('guardian-war-ukraine.csv')
df.to_json('guardian-war-ukraine.json')
