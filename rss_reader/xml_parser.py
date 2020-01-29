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
        :rtype: List[NewsItem]
        """
        root = ET.fromstring(data)
        channel = root.find('channel')
        channel_title = channel.find('title').text
        print(channel_title)
        channel_link = channel.find('link').text
        print(channel_link)
        channel_desc = channel.find('description').text
        print(channel_desc)
        self.db_helper.add_channel(channel_title, channel_link, channel_desc)
        for x in channel.findall('item'):
            item_title = x.find('title')
            if item_title is None:
                continue
            item_title = item_title.text
            print(item_title)

