from opp.miner.field import Field
from opp.miner.view import View


class Controller:
    def __init__(self):
        self.field = Field()
        self.field.generate_field()
        self.view = View(self.field)

    def start_game(self):
        self.view.display_field()
        x = int(input("x: "))
        y = int(input("y: "))
        self.field.open_cell(x, y)
        self.view.display_field()

ctrl = Controller()
