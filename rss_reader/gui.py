# window
from PyQt5.QtWidgets import QGridLayout, QListWidget, QWidget, QApplication, QPushButton, QInputDialog

from rss_reader.controller import Controller


class Window(QWidget):
    def __init__(self, ctrl):
        super().__init__()
        self.controller = ctrl  # type: Controller
        self.initUI()

    def initUI(self):
        grid = QGridLayout()

        self.news_list = QListWidget(self)
        grid.addWidget(self.news_list, 0, 0, 3, 6)

        self.channel_list = QListWidget(self)
        grid.addWidget(self.channel_list, 0, 6, 2, 3)

        self.add_channel = QPushButton(self, text="Add channel")
        self.add_channel.clicked.connect(self.show_add_channel)
        grid.addWidget(self.add_channel, 5, 5)

        self.update_news = QPushButton(self, text="Update")
        self.update_news.clicked.connect(self.controller.update_news)
        grid.addWidget(self.update_news, 5, 4)

        self.setLayout(grid)
        self.setGeometry(100, 100, 800, 500)

    def show_add_channel(self):
        dialog = QInputDialog(self)
        item, ok = dialog.getText(self, "Add channel", "Channel url:")
        if ok:
            self.controller.add_source(item)


    def update_news_list(self, values):
        """
        Обновление списка новостей (полностью)
        :param values:
        :return:
        """
        self.news_list.clear()
        for value in values:
            self.news_list.addItem(value.title)

    def update_source_list(self, values):
        """
        Обновление списка контактов (полностью)
        """
        self.channel_list.clear()
        for value in values:
            self.channel_list.addItem(value.title)


if __name__ == '__main__':
    app = QApplication([])
    ctrl = Controller()
    window = Window(ctrl)
    window.show()
    app.exec_()