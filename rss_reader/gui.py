# window
from rss_reader.controller import Controller


class Window:
    def __init__(self):
        self.controller = None  # type: Controller

    def update_news_list(self, values):
        """
        Обновление списка новостей (полностью)
        :param values:
        :return:
        """
        pass

    def update_source_list(self, values):
        """
        Обновление списка контактов (полностью)
        """
        pass
