from tictactoe.field import Field, Cell
from tictactoe.player import HumanPlayer
from tictactoe.view import View


class Controller:
    def start_game(self):
        field = Field(3)
        view = View(field)
        first = HumanPlayer(Cell.CROSS)
        second = HumanPlayer(Cell.ZERO)

        current_player = first
        while True:
            view.show_field()
            x, y = current_player.make_turn(field)
            if field.set_value(x, y, current_player.sign):
                check_result = field.check_field()
                if check_result != Cell.EMPTY:
                    print(current_player.sign, 'wins')
                    view.show_field()
                    break
                if field.is_full():
                    print('draw')
                    view.show_field()
                    break
                if current_player == first:
                    current_player = second
                else:
                    current_player = first
            else:
                print("Please retry!")



