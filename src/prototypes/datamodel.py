from enum import Enum


class Publishers(Enum):
    KATHIMERINI = 'ΚΑΘΗΜΕΡΙΝΗ'
    EFSYN = 'ΕΦΗΜΕΡΙΔΑ ΤΩΝ ΣΥΝΤΑΚΤΩΝ'
    NAFTEMPORIKI = 'ΝΑΥΤΕΜΠΟΡΙΚΗ'
    THE_GUARDIAN = 'THE GUARDIAN'


class Lang(Enum):
    ENGLISH = 'en'
    GREEK = 'el'


class Sentiments(Enum):
    NEGATIVE = 'negative'
    POSITIVE = 'positive'
    NEUTRAL = 'neutral'


class DataModel(Enum):
    ARTICLE_PUBLISHER = 'Publisher'
    ARTICLE_TAG = 'Tag'
    ARTICLE_URL = 'Article url'
    ARTICLE_HEADING = 'Heading'
    ARTICLE_TEXT = 'Text'
    ARTICLE_ABSTRACT = 'Summary'
    ARTICLE_DATE_TIME = 'Date Formatted'
    ARTICLE_IMAGE_URL = 'Image url'
    ARTICLE_IMAGE_CAPTION = 'image caption'
    ARTICLE_HAS_COMMENTS = 'Comments exist'
    ARTICLE_COMMENT_COUNT = 'Comments count'
    ARTICLE_COMMENT_API_KEY = 'Comments api key'
    ARTICLE_COMMENT_URL = 'Comments url'
    ARTICLE_LANG = 'Lang'
    ARTICLE_DATE_FORMAT_READY = 'Date Formatted'


class ArticleModel:
    publisher = DataModel.ARTICLE_PUBLISHER.value
    date = DataModel.ARTICLE_DATE_FORMAT_READY.value
    comments = DataModel.ARTICLE_HAS_COMMENTS.value
    commentApiKey = DataModel.ARTICLE_COMMENT_API_KEY.value
    commentsCount = DataModel.ARTICLE_COMMENT_COUNT.value
    commentsUrl = DataModel.ARTICLE_COMMENT_URL.value
    lang = DataModel.ARTICLE_LANG.value
    url = DataModel.ARTICLE_URL.value
    heading = DataModel.ARTICLE_HEADING.value
    summary = DataModel.ARTICLE_ABSTRACT.value
    tag = DataModel.ARTICLE_TAG.value
    text = DataModel.ARTICLE_TEXT.value
    imageUrl = DataModel.ARTICLE_IMAGE_URL.value
