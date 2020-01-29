from datetime import datetime
import dateparser
from rss_reader.database_helper import NewsItem, DBHelper
from typing import List
import xml.etree.ElementTree as ET


class XmlParser:
    def __init__(self, db_helper):
        self.db_helper = db_helper

    def parse_xml(self, data):
        """
        Разбирает строку на список готовых объектов
        :param data:
        """
        root = ET.fromstring(data)
        channel = root.find('channel')
        channel_title = channel.find('title').text
        channel_link = channel.find('link').text
        channel_desc = channel.find('description').text
        self.db_helper.add_channel(channel_title, channel_link, channel_desc)
        channel_info = self.db_helper.get_channel_id_by_title(channel_title)
        news = []
        for x in channel.findall('item'):
            item_title = self.get_item_property(x, 'title')
            item_desc = self.get_item_property(x, 'description')
            item_link = self.get_item_property(x, 'link')
            item_date = self.get_item_property(x, 'pubDate')
            if item_desc is not None and item_title is not None and item_link is not None and item_date is not None:
                news.append({'title': item_title, 'date': dateparser.parse(item_date), 'desc': item_desc, 'channel': channel_info})
        self.db_helper.add_news(news)

    def get_item_property(self, element, tag):
        title = element.find(tag)
        if title is not None:
            return title.text



