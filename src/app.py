from typing import Union, Any
from bs4 import BeautifulSoup
from endpoints import Endpoints
from datetime import datetime
from utilities import Utilities
import requests
import re

NOT_FOUND: None = None


class GuardianScraper:

    @staticmethod
    def getCommentCount(key: str) -> Any:
        """

        :type key: str
        """
        try:
            s = requests.Session()
            response = s.get(f'{Endpoints.THE_GUARDIAN_DISCUSSION_API.value}{key}')
            data = response.json()
            return data['discussion']['commentCount']
        except:
            return NOT_FOUND

    @staticmethod
    def getDiscussionKey(url: str) -> str:
        """

        :type url: str
        """
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

    @staticmethod
    def getRawHTML(url: str) -> object:
        """

        :type url: str
        """
        s = requests.Session()
        response = s.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        return soup

    @staticmethod
    def getArticleImage(url: str) -> object:
        s = requests.Session()
        response = s.get(url)
        article_page = BeautifulSoup(response.text, 'html.parser')
        try:
            figures = article_page.find_all('figure')
            for figure in figures:
                image = figure.find('img')
                image_url = image['src']
                image_alt = image['alt']
                caption_spans = figure.find('figcaption').children
                image_caption = ' '.join(str(child.text.strip()) for child in caption_spans)
                image = {
                    'alt': image_alt,
                    'caption': image_caption,
                    'url': image_url
                }
                return image
        except:
            return NOT_FOUND

    @staticmethod
    def getArticleText(url: str) -> str:
        """

        :type url: str
        """
        s = requests.Session()
        response = s.get(url)
        single_page = BeautifulSoup(response.text, 'html.parser')
        try:
            paragraphs = single_page.find('div', attrs={'class': 'article-body-commercial-selector'}).children
            text = ' '.join(str(child.text.strip()) for child in paragraphs)
        except:
            try:
                article_blocks_body = single_page.find('div', attrs={'id': 'liveblog-body'})
                blocks = article_blocks_body.find_all('article')
                text = ' '.join(str(child.text.strip()) for child in blocks)
            except:
                try:
                    media_body = single_page.find('div', attrs={'class': 'media-body'})
                    media_body_paragraphs = media_body.find_all('p')
                    text = ' '.join(str(child.text.strip()) for child in media_body_paragraphs)
                except:
                    text = NOT_FOUND
        return text

    @staticmethod
    def getNextUrl(soup: object, currentUrl: str) -> str:
        """

        :param currentUrl:
        :type soup: object
        """
        url = ''
        try:
            pages = soup.find('div', attrs={'class': 'pagination u-cf'})
            if pages.find('a', attrs={'class': 'pagination__action--pushleft', 'rel': 'next'}):
                nextUrl = str(pages.find('a', attrs={'class': 'pagination__action--pushleft'})['href'])
                print('nextUrl: ', nextUrl)
                url = nextUrl
            else:
                print('currentUrl: ', currentUrl)
                url = NOT_FOUND
        except:
            print('***NEXT URL NOT FOUND: ', currentUrl)
            url = NOT_FOUND
        finally:
            return url

    @staticmethod
    def transformHTMLtoObject(soup: object) -> list:
        """

        :type soup: bs4.BeautifulSoup
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
            text = GuardianScraper.getArticleText(link)
            article_image: object = GuardianScraper.getArticleImage(link)
            if not article_image:
                article_image_url = NOT_FOUND
                article_image_alt = NOT_FOUND
                article_image_caption = NOT_FOUND
            else:
                article_image_url = article_image['url']
                article_image_alt = article_image['alt']
                article_image_caption = article_image['caption']
            try:
                image = article.find('img', {'class': 'responsive-img'})['src']
            except:
                image = NOT_FOUND
            try:
                comment_url = article.find_parent('div', attrs={'data-discussion-closed': 'true'})[
                    'data-discussion-url']
            except:
                comment_url = NOT_FOUND

            if comment_url:
                comment_key = GuardianScraper.getDiscussionKey(comment_url)
                comment_count = GuardianScraper.getCommentCount(comment_key)
            else:
                comment_key = NOT_FOUND
                comment_count = NOT_FOUND
            data = {
                'Image Url': article_image_url,
                'Image Caption': article_image_caption,
                'Image Alt': article_image_alt,
                'Date': dateFull,
                'Date Formatted': dateObject,
                'Heading': heading,
                'Article Url': link,
                'Text': text,
                'Comments key': comment_key,
                'Comments Count': comment_count,
                'Comments Url': comment_url,
                'Thumb': image,
            }
            articles_dict.append(data)
        return articles_dict


class GuardianCommentsAPI:

    @staticmethod
    def getCommentsByCommentKey(key: str, page: int) -> object:
        """

        :type page: int
        :param page:
        :type key: str
        :param key:
        """
        url = f'{Endpoints.THE_GUARDIAN_DISCUSSION_API.value}{key}?page={page}&pageSize=100'
        print(url)
        try:
            s = requests.Session()
            response = s.get(url)
            comments = response.json()
            data = comments
        except:
            data = NOT_FOUND
        finally:
            return data
        # :path: / discussion - api / discussion / p / kz8t5?api - key = dotcom - rendering & orderBy = oldest & pageSize = 100 & displayThreaded = true & maxResponses = 3 & page = 1

    @staticmethod
    def apiResponseToDictionary(response: object) -> list:
        comments = []
        for comment in response['discussion']['comments']:
            if not (comment.get('responses') is None):
                replies = comment.get('responses')
                responses = True
                responses_count = len(replies)
                for reply in replies:
                    reply_dict = dict(
                        responseId=reply['id'],
                        responseText=Utilities.fromHTMLtoText(reply['body']),
                        date=reply['date'],
                        isoDateTime=reply['isoDateTime'],
                        numRecommends=reply['numRecommends'],
                        responseTo=reply['responseTo']['displayName'],
                        commentId=reply['responseTo']['commentId'],
                        commentWebUrl=reply['responseTo']['commentWebUrl']

                    )
            else:
                responses = False
                responses_count = 0
                reply_dict = NOT_FOUND

            data = dict(Title=response['discussion']['title'],
                        key=response['discussion']['key'],
                        commentCount=response['discussion']['commentCount'],
                        webUrl=response['discussion']['webUrl'],
                        apiUrl=response['discussion']['apiUrl'],
                        discussionId=comment['id'],
                        date=comment['date'],
                        isoDateTime=comment['isoDateTime'],
                        text=Utilities.fromHTMLtoText(comment['body']),
                        userId=comment['userProfile']['userId'],
                        displayName=comment['userProfile']['displayName'],
                        numRecommends=comment['numRecommends'],
                        isThreaded=response['discussion']['isThreaded'],
                        responses=responses,
                        responsesCount=responses_count,
                        replies=reply_dict)
            comments.append(data)
        return comments


class efsynScraper:

    @staticmethod
    def getArticles(url: str) -> list:
        articles_data = []
        s = requests.Session()
        response = s.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        try:
            articles = soup.find_all('article', attrs={'class': 'default-teaser__article'})
            for article in articles:
                tag = article.find('a', attrs={'class': 'default-teaser__cat'}).text.strip()
                datetime = article.find('time', attrs={'class': 'default-date'}).text.split(",")
                date = datetime[0]
                time = datetime[1].replace(" ", "")
                heading = article.find('div', attrs={'class': 'default-teaser__title'}).text.strip()
                article_url = article.find('a', attrs={'class': 'full-link'})['href']
                full_url = f'{Endpoints.EFSYN_BASE_URL.value}{article_url}'
                article_soup = efsynScraper.getArticleContent(full_url)
                text = efsynScraper.getFullText(article_soup)
                image_url = efsynScraper.getArticleImage(article_soup)
                if not image_url:
                    image_url = NOT_FOUND

                data = dict(tag=tag,
                            date=date,
                            time=time,
                            heading=heading,
                            url=full_url,
                            text=text,
                            image_url=image_url
                            )
                articles_data.append(data)
        except:
            articles_data = []
        finally:
            return articles_data

    @staticmethod
    def getArticleContent(url: str) -> str:
        s = requests.Session()
        response = s.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        return soup

    @staticmethod
    def getFullText(soup: object):
        try:
            paragraphs = soup.find('div', attrs={'class': 'article__body'}).find_all('p')
            text = ' '.join(str(child.text.strip()) for child in paragraphs)
        except:
            text = NOT_FOUND
        finally:
            return text

    @staticmethod
    def getArticleImage(soup: object) -> str:
        try:
            image = soup.find('figure', attrs={'class': 'article__media'})
            image_url = image.find('img')['src']
            image_url_full = f'{Endpoints.EFSYN_BASE_URL.value}{image_url}'
            # caption = image.find('figcaption').find('p').text.strip()
            data = image_url_full

        except:
            data = NOT_FOUND
        finally:
            return data


class kathimeriniScraper:

    @staticmethod
    def getPageContent(url: str) -> object:
        s = requests.Session()
        response = s.get(url)
        print(f'GET: url => {url}')
        soup = BeautifulSoup(response.content, "html.parser")
        return soup

    @staticmethod
    def getArticleText(soup: object) -> str:
        try:
            paragraphs = soup.find('div', attrs={'class': 'entry-content'}).find_all('p')
            full_text = ' '.join(str(child.text.strip()) for child in paragraphs)
            cleanText = Utilities.fromHTMLtoText(full_text)
        except:
            cleanText = NOT_FOUND
        finally:
            return cleanText

    @staticmethod
    def getDateTime(soup: object) -> dict:
        try:
            raw_date = soup.find('span', attrs={'class': 'meta-date'})
            date = raw_date.find('time').text.replace("•", "")
            dateUTC = raw_date.find('time')['datetime']
            date = dict(
                date=date,
                dateUTC=dateUTC
            )
        except:
            date = NOT_FOUND
        finally:
            return date

    @staticmethod
    def constructData(article: object) -> dict:
        url = article.find('div', attrs={'class': 'article_thumbnail_wrapper'}).find('a')['href']
        heading = article.find('h2').text.strip()
        summary = article.find('p').text.strip()
        tag = article.find('span', attrs={'class': 'headlines'}).text.strip()
        soup = kathimeriniScraper.getPageContent(url)
        full_text = kathimeriniScraper.getArticleText(soup)
        try:
            date = kathimeriniScraper.getDateTime(soup)
            dateUTC = date.get("dateUTC")
            date = date.get("date")
        except:
            dateUTC = NOT_FOUND
            date = NOT_FOUND

        data = dict(url=url,
                    heading=heading,
                    summary=summary,
                    tag=tag,
                    full_text=full_text,
                    dateUTC=dateUTC,
                    date=date)
        return data


class naftemporikiScraper:

    @staticmethod
    def constructData(article: object) -> dict:
        try:
            heading = article\
                .find('div', attrs={'class': 'storyHeader'})\
                .find('h3').find('a')\
                .text.strip()
            url = article\
                .find('div', attrs={'class': 'storyHeader'})\
                .find('h3')\
                .find('a')['href']
            full_url = f'{Endpoints.NAFTEMPORIKI_BASE_URL.value}{url}'
            date = article\
                .find('div', attrs={'class': 'storyHeader'})\
                .find('span', attrs={'class': 'date'})\
                .text.replace("-", "")
            tag = article\
                .find('div', attrs={'class': 'storyHeader'})\
                .find('span', attrs={'class': 'stream-categ'})\
                .find('a').text.strip()
            soup = naftemporikiScraper.getPageContent(full_url)
            text = naftemporikiScraper.getFullText(soup)
            image = naftemporikiScraper.getImage(soup)
            data = dict(url=full_url,
                        heading=heading,
                        date=date,
                        tag=tag,
                        text=text,
                        image=image
                        )
        except:
            data = NOT_FOUND
        finally:
            return data

    @staticmethod
    def getPageContent(url: str) -> object:
        s = requests.Session()
        response = s.get(url)
        print(f'GET: url => {url}')
        soup = BeautifulSoup(response.content, "html.parser")
        return soup

    @staticmethod
    def getFullText(soup: object) -> str:
        try:
            paragraphs = soup.find('span', attrs={'id': 'spBody'}).find_all('p')
            text = ' '.join(str(child.text.strip()) for child in paragraphs)
            cleanText = Utilities.fromHTMLtoText(text)
        except:
            cleanText = NOT_FOUND
        finally:
            return cleanText

    @staticmethod
    def getImage(soup: object):
        try:
            image = soup\
                .find('div', attrs={'class': 'storyMediaContent'})\
                .find('img')['src']
            image_url = f'{Endpoints.NAFTEMPORIKI_BASE_URL.value}{image}'
        except:
            image_url = NOT_FOUND
        finally:
            return image_url


class ImageDownloader:

    @staticmethod
    def getImage(url, filename):
        response = requests.get(url, stream=True)
        if response.status_code == 200:
            with open('../data/images/' + filename + '.jpg', 'wb') as jpg:
                jpg.write(response.content)
            print('Image sucessfully Downloaded: ', filename)
        else:
            print('Image Couldn\'t be retrieved')


class ParserHTML:

    @staticmethod
    def readRawHTML(path: str) -> object:
        """

        :type path: str
        """
        with open(path) as file:
            soup = BeautifulSoup(file, "html.parser")
            return soup
