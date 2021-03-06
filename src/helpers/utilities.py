import re
import string


class Utilities:

    @staticmethod
    def fromHTMLtoText(html):
        text = re.compile('<.*?>')
        cleantext = re.sub(text, '', html).strip()
        return cleantext

    @staticmethod
    def convertToKebapCase(string: str) -> str:
        """

        :type string: str
        """
        s = string \
            .replace('"', '') \
            .replace(',', '') \
            .replace("'", "") \
            .replace(".", "") \
            .replace("’", "") \
            .replace("/", "") \
            .replace(":", "") \
            .replace("&", "")
        return '-'.join(
            re.sub(r"(\s|_|-)+", " ",
                   re.sub(r"[A-Z]{2,}(?=[A-Z][a-z]+\d*|\b)|[A-Z]?[a-z]+\d*|[A-Z]|\d+",
                          lambda mo: ' ' + mo.group(0).lower(), s)).split())

    @staticmethod
    def extractDateFromDatetime(string: str) -> str:
        try:
            match = re.search(r'\d{2}(?:.|-|/)\d{2}(?:.|-|/)\d{4}', string)
            date = match.group() \
                .replace(".", "-") \
                .replace("/", "-")
        except:
            date = None
        finally:
            return date

    @staticmethod
    def reverseDateString(string: str) -> str:
        try:
            reverse = "-".join(reversed(string.split("-")))
            print(reverse)
        except:
            reverse = None
        finally:
            return reverse

    @staticmethod
    def getFirstParamFromUrl(string: str) -> str:
        """

        :type string: str
        """
        try:
            match = string.split("/")[3] \
                .replace("-", " ") \
                .upper()
        except:
            match = None
        finally:
            return match

    @staticmethod
    def removeURL(string: str) -> str:
        try:
            clean = re.sub('http://\S+|https://\S+', '', string)
        except:
            clean = ''
        finally:
            return clean

    @staticmethod
    def removePunctuation(text: str) -> str:
        """

        :type text: str
        """
        text = re.sub(r'[' + string.punctuation + '’—”' + ']', ' ', text.lower())
        return re.sub(r'\W', ' ', text)

    @staticmethod
    def removeAccents(text: str) -> str:
        """

        :type text: str
        """
        return (text
                .replace("ύ", "υ")
                .replace("ά", "α")
                .replace("ί", "ι")
                .replace("ώ", "ω")
                .replace("έ", "ε")
                .replace("ό", "ο")
                .replace("εί", "ει")
                .replace("ή", "η")
                .replace("ού", "ου")
                )

    @staticmethod
    def removeHashtag(text: str) -> str:
        return re.sub("#\S+", "", text)

    @staticmethod
    def removeMention(text: str) -> str:
        return re.sub("@\S+", "", text)

    @staticmethod
    def removeLineBreaks(text: str) -> str:
        return re.sub("\n+", "", text)

    @staticmethod
    def removeRT(string: str) -> str:
        try:
            clean = re.sub('RT', '', string)
        except:
            clean = ''
        finally:
            return clean

    @staticmethod
    def removeUnicode(text: str) -> str:
        """

        :type text: str
        """
        return (text
                .replace("amp", "")
                )

    @staticmethod
    def trimWhiteSpaces(text: str) -> str:
        return " ".join(text.split())


