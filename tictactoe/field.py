class Cell:
    ZERO = '0'
    CROSS = 'X'
    EMPTY = '_'


class Field:
    def __init__(self, size=3):
        self.size = size
        self.data = [[Cell.EMPTY for x in range(self.size)] for y in range(self.size)]
        self.length = 3 if self.size < 5 else 5
        self.filled_count = 0

    def set_value(self, x, y, value):
        if x < 0 or y < 0 or x >= self.size or y >= self.size:
            return False
        if self.data[x][y] != Cell.EMPTY:
            return False
        self.data[x][y] = value
        self.filled_count += 1
        return True

    def is_full(self):
        return self.filled_count == self.size * self.size

    def check_field(self):
        for x in range(self.size):
            for y in range(self.size):
                check_result = self._check_row(x, y, self.length)
                if check_result != Cell.EMPTY:
                    return check_result
                check_result = self._check_column(x, y, self.length)
                if check_result != Cell.EMPTY:
                    return check_result
                check_result = self._check_diagonal(x, y, self.length)
                if check_result != Cell.EMPTY:
                    return check_result
                check_result = self._check_back_diagonal(x, y, self.length)
                if check_result != Cell.EMPTY:
                    return check_result
        return Cell.EMPTY

    def get_value(self, x, y):
        return self.data[x][y]

    def _check_row(self,x ,y, length=3):
        if y + length - 1 < self.size:
            for i in range(length - 1):
                if self.data[x][y + i] != self.data[x][y + i + 1]:
                    return Cell.EMPTY
            return self.data[x][y]
        return Cell.EMPTY

    def _check_column(self, x, y, length=3):
        if x + length - 1 < self.size:
            for i in range(length - 1):
                if self.data[x + i][y] != self.data[x + i + 1][y]:
                    return Cell.EMPTY
            return self.data[x][y]
        return Cell.EMPTY

    def _check_diagonal(self, x, y, length=3):
        if x + length - 1 < self.size and y + length - 1 < self.size:
            for i in range(length - 1):
                if self.data[x + i][y + i] != self.data[x + i + 1][y + i + 1]:
                    return Cell.EMPTY
            return self.data[x][y]
        return Cell.EMPTY

    def _check_back_diagonal(self, x, y, length=3):
        if x + length - 1 < self.size and y - length + 1 >= 0:
            for i in range(length - 1):
                if self.data[x + i][y - i] != self.data[x + i + 1][y - i - 1]:
                    return Cell.EMPTY
            return self.data[x][y]
        return Cell.EMPTY