'''from rss_reader.gui import Window
from rss_reader.xml_parser import XmlParser
from rss_reader.database_helper import DBHelper
from rss_reader.content_loader import ContentLoader'''
from rss_reader.content_loader import ContentLoader
from rss_reader.database_helper import DBHelper
from rss_reader.xml_parser import XmlParser


class Controller:
    def __init__(self):
        self.db = DBHelper()
        self.content_loader = ContentLoader()
        self.news_item = XmlParser(self.db)

    def add_source(self, value):
        print(type(value))
        print(value)
        # self.db.add_channel(value,'','')
        self.view.update_source_list([])
        """
        Добавление нового источника
        :param value:
        :return:
        """

    def remove_source(self, value):

        """
        Удаляет источник из списка текущих и базы
        :param value:
        :return:
        """
        pass

    def update_news(self):
        """
        Загружаем RSS, разбираем его и обновляем View
        :return:
        """
        data = self.content_loader.load_page(self.db.get_channels)
        self.news_item.parse_xml(data)
        self.view.update_news_list(self.db.get_news())

    def set_view(self, window):
        self.view = window
