import requests


class ContentLoader:
    def load_page(self, url):
        """
        Загружает содержимое страницы (исходный код)
        :param url:
        :rtype: str
        """
        return requests.get(url).content.decode('utf-8')
