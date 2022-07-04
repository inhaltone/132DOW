import re


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
        s = string\
            .replace('"', '')\
            .replace(',', '')\
            .replace("'", "")\
            .replace(".", "")\
            .replace("’", "")\
            .replace("/", "")\
            .replace(":", "")\
            .replace("&", "")
        return '-'.join(
            re.sub(r"(\s|_|-)+", " ",
                   re.sub(r"[A-Z]{2,}(?=[A-Z][a-z]+\d*|\b)|[A-Z]?[a-z]+\d*|[A-Z]|\d+",
                          lambda mo: ' ' + mo.group(0).lower(), s)).split())
