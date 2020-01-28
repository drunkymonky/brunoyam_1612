from abc import ABC, abstractmethod


class AbstractPlayer(ABC):
    def __init__(self, sign):
        self.sign = sign

    @abstractmethod
    def make_turn(self, field):
        pass


class HumanPlayer(AbstractPlayer):
    def __init__(self, sign):
        super().__init__(sign)

    def make_turn(self, field):
        while True:
            try:
                coords = tuple(map(int, input('Enter turn: ').split(' ')))
                return coords
            except ValueError:
                print('Input error. Try again')