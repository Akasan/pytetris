import numpy as np


class Board:
    def __init__(self, width: int = 10, height: int = 20):
        self.WIDTH = width
        self.HEIGHT = height
        self._init_board()

    def _init_board(self):
        self.board = np.zeros((self.HEIGHT, self.WIDTH))

    def is_full(self, row: int) -> bool:
        return np.all(self.board[row, :] == 1)

    def set(self, row: int, col: int):
        self.board[row, col] = 1

    def clear(self, row: int, col: int):
        self.board[row, col] = 0

board = Board()
for i in range(10):
    board.set(0, i)

print(board.board)
