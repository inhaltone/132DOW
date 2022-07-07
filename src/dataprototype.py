from enum import Enum


class ArticleDataModel(Enum):
    ARTICLE_PUBLISHER = 'publisher'
    ARTICLE_TAG = 'tag'
    ARTICLE_URL = 'article url'
    ARTICLE_HEADING = 'heading'
    ARTICLE_TEXT = 'text'
    ARTICLE_DATE_TIME = 'date'
    ARTICLE_IMAGE_URL = 'image URL'
    ARTICLE_IMAGE_CAPTION = 'image caption'
    ARTICLE_HAS_COMMENTS = 'comments'
    ARTICLE_COMMENT_COUNT = 'comment count'
    ARTICLE_COMMENT_KEY = 'comment key'
    ARTICLE_COMMENT_URL = 'comments url'
