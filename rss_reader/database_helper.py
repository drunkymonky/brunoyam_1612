from pony.orm import *
from datetime import datetime
from typing import List

db = Database()
db.bind(provider='sqlite', filename='db.sqlite', create_db=True)

class NewsItem(db.Entity):
    id = PrimaryKey(int, auto=True)
    title = Required(str)
    date = Required(datetime)
    desc = Required(str)


class ChanelItem(db.Entity):
    id = PrimaryKey(int, auto=True)
    title = Required(str)
    link = Required(str)
    desc = Required(str)


db.generate_mapping(create_tables=True)


class DBHelper:
    def add_news(self, values):
        """
        :type values: List[NewsItem]
        :return:
        """
        pass

    @db_session
    def add_channel(self, title, link, desc):
        if ChanelItem.get(title=title) is None:
            ChanelItem(title=title, link=link, desc=desc)

    @db_session
    def get_news(self, count=100):
        """
        Возвращает список всех новостей, отсортированные по дате
        :rtype: List[NewsItem]
        """
        pass

