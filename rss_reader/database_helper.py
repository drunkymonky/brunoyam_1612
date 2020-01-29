from pony.orm import *
from datetime import datetime
from typing import List

db = Database()
db.bind(provider='sqlite', filename='db.sqlite', create_db=True)


class ChannelItem(db.Entity):
    id = PrimaryKey(int, auto=True)
    title = Required(str)
    link = Required(str)
    desc = Required(str)
    news = Set('NewsItem')


class NewsItem(db.Entity):
    id = PrimaryKey(int, auto=True)
    title = Required(str)
    date = Required(datetime)
    desc = Required(str)
    channel = Required(ChannelItem)


db.generate_mapping(create_tables=True)


class DBHelper:
    @db_session
    def add_news(self, values):
        """
        :type values: List[NewsItem]
        :return:
        """
        # TODO do not add same news
        for value in values:
            channel_data = ChannelItem.get(id=value['channel'])
            NewsItem(title=value['title'], desc=value['desc'], date=value['date'], channel=channel_data)

    @db_session
    def add_channel(self, title, link, desc):
        current_channel = ChannelItem.get(title=title)
        if current_channel is None:
            return ChannelItem(title=title, link=link, desc=desc)
        return current_channel

    @db_session
    def get_channel_id_by_title(self, title):
        return ChannelItem.get(title=title).id

    @db_session
    def get_news(self, count=100):
        """
        Возвращает список всех новостей, отсортированные по дате
        :rtype: List[NewsItem]
        """
        return select(p for p in NewsItem)[:]


    @db_session
    def get_channels(self):
        return select(p for p in ChannelItem)[:]

