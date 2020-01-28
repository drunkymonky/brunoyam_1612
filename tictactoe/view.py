from tictactoe.field import Cell


class View:
    def __init__(self, field):
        self.field = field

    def show_field(self):
        for i in range(self.field.size):
            for j in range(self.field.size):
                print(self.field.get_value(i, j), end=' ')
            print()

