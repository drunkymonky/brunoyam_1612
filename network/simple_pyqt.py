from PyQt5.QtWidgets import QApplication, QLineEdit, QGridLayout, QWidget, QListWidget, QPushButton


class PyQtWindow(QWidget):
    def __init__(self, action_send):
        super().__init__()
        self.action = action_send
        self.initUI()

    def initUI(self):
        grid = QGridLayout()

        self.list = QListWidget(self)
        self.list.addItem('Hello')
        grid.addWidget(self.list, 0, 0, 3, 4)

        self.user_input = QLineEdit()
        grid.addWidget(self.user_input, 3, 0, 1, 3)

        self.send_button = QPushButton()
        self.send_button.setText("Send")
        self.send_button.clicked.connect(self.button_clicked)
        grid.addWidget(self.send_button, 3, 3)

        self.setLayout(grid)
        self.setGeometry(100, 100, 400, 400)

    def button_clicked(self):
        text = self.user_input.text()
        self.user_input.clear()
        self.action(bytes(text, 'utf-8'))

    def add_input(self, value):
        self.list.insertItem(self.list.count(), value)


if __name__ == '__main__':
    app = QApplication([])
    window = PyQtWindow(lambda x: print(x))
    window.show()
    app.exec_()
