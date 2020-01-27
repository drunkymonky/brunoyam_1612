class Controller:
    def __init__(self):
        self.db = None
        self.view = None
        self.content_loader = None

    def add_source(self, value):
        """
        Добавление нового источника
        :param value:
        :return:
        """
        pass

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
        pass
