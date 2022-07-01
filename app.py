from typing import Union, Any
from bs4 import BeautifulSoup
import requests
import re
from endpoints import Endpoints


def getCommentCount(key):
    try:
        s = requests.Session()
        response = s.get(f'{Endpoints.THE_GUARDIAN_DISCUSSION_API.value}{key}')
        data = response.json()
        return data['discussion']['commentCount']
    except:
        return None


def getDiscussionKey(url):
    s = requests.Session()
    response = s.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    scripts = soup.find_all('script')
    for script in scripts:
        script_with_key = script.getText().strip().__contains__('window.guardian = {"config":{')
        if script_with_key:
            text = script.getText().strip()
            discussion_key: Union[str, Any] = re.search('"shortUrlId":"(.*?)"', text).group(1)
            return discussion_key


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
