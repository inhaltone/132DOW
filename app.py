from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import json
# from requests_html import HTMLSession
import requests
import re
# data-discussion-url

def sample():
    browser = webdriver.Firefox()
    browser.get('https://www.theguardian.com/politics/2022/feb/23/putins-looming-threat-gives-johnson-some-breathing-space#comments')
    # vegetable = driver.find_element(By.CLASS_NAME, "tomatoes")


# sample()
def getCommentCount(key):
    api_url = 'https://discussion.theguardian.com/discussion-api/discussion'
    s = requests.Session()
    response = s.get(f'{api_url}{key}')
    data = response.json()
    print(data['discussion']['commentCount'])

def getDiscussionKey(url):
    s = requests.Session()
    response = s.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    scripts = soup.find_all('script')
    for script in scripts:
        script_with_key = script.getText().strip().__contains__('window.guardian = {"config":{')
        if script_with_key:
            text = script.getText().strip()
            try:
                discussion_key = re.search('"shortUrlId":"(.*?)"', text).group(1)
                print(discussion_key)
                return discussion_key
            except:
                return None



key = getDiscussionKey('https://www.theguardian.com/politics/2022/feb/23/putins-looming-threat-gives-johnson-some-breathing-space#comments')
if key:
    getCommentCount(key)


def getRawHTML(url) -> object:
    s = requests.Session()
    response = s.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    return soup


def getArticleText(url: object) -> object:
    s = requests.Session()
    response = s.get(url)
    single_page = BeautifulSoup(response.text, 'html.parser')
    try:
        paragraphs = single_page.find('div', attrs={'class': 'article-body-commercial-selector'}).children
        text = ' '.join(str(child.text.strip()) for child in paragraphs)
        return text
    except:
        text = ''
        return text


def getNextUrl(soup):
    """

    :type soup: object
    """
    pages = soup.find('div', attrs={'class': 'pagination u-cf'})
    if pages.find('a', attrs={'class': 'pagination__action--pushleft', 'rel': 'next'}):
        url = str(pages.find('a', attrs={'class': 'pagination__action--pushleft'})['href'])
        return url
    else:
        return



