from pony.orm import *
from typing import List


class NewsItem:
    title = Required(str)
    date = Required(str)
    desc = Required(str)


class XmlParser:
    def parse_xml(self, data):
        """
        Разбирает строку на список готовых объектов
        :param data:
        :rtype: List[NewsItem]
        """
        pass