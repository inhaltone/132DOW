import pandas as pd
from bs4 import BeautifulSoup
from requests_html import HTMLSession
from app import getRawHTML, getNextUrl, getArticleText, getCommentCount
from datetime import datetime

FULL_URL = 'https://www.theguardian.com/world/ukraine/2022/feb/23/all'
NOT_FOUND = None
s = HTMLSession()
guardian_df = pd.DataFrame()
articles_data = []
count = 0
df = pd.DataFrame()


def transformHTMLtoObject(soup: object) -> object:
    """

    :rtype: object
    """
    articles_dict = []
    articles = soup.find_all('div', {'class': 'fc-item__container'})
    day = soup.find('span', {'class': 'fc-today__dayofweek'}).text.strip()
    daymonth = soup.find('span', {'class': 'fc-today__dayofmonth'}).text.strip()
    month = soup.find('span', {'class': 'fc-today__month'}).text.strip()
    year = soup.find('span', {'class': 'fc-today__year'}).text.strip()
    dateFull = f'{day}, {daymonth} {month} {year}'
    dateObject = datetime.strptime(f'{year}-{month}-{daymonth}', '%Y-%B-%d').date()
    for article in articles:
        heading = article.find('a', {'class': 'u-faux-block-link__overlay'}).text.strip()
        link = article.find('a', {'class': 'u-faux-block-link__overlay'})['href']
        # get the full article text
        text = getArticleText(link)
        try:
            image = article.find('img', {'class': 'responsive-img'})['src']
        except:
            image = NOT_FOUND
        try:
            comment_url = article.find_parent('div', attrs={'data-discussion-closed': 'true'})['data-discussion-url']
            comment_count = getCommentCount(comment_url)
        except:
            comment_url = NOT_FOUND
        data = {
            'comment count': comment_count,
            'comments': comment_url,
            'dateFull': dateFull,
            'date': dateObject,
            'heading': heading,
            'link': link,
            'image': image,
            'text': text
        }
        print(data)
        articles_dict.append(data)
    return articles_dict


while True:
    RAW_HTML = getRawHTML(FULL_URL)
    FULL_URL = getNextUrl(RAW_HTML)
    print(FULL_URL)
    articles_data = transformHTMLtoObject(RAW_HTML)
    df = pd.concat([df, pd.DataFrame(articles_data)], axis=0)
    count += 1
    print(f'========================================= {count} =======================================')
    # print(len(articles_data))
    if count > 2:
        break

df.to_csv('data/test6-21.csv')
print(df.head())
