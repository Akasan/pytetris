import numpy as np
from shape import ShapeBase, OShape


class Board:
    def __init__(self, width: int = 10, height: int = 20):
        self.WIDTH = width
        self.HEIGHT = height
        self._init_board()
        self.pre_board = None
        self.upper_left_col = None
        self.upper_left_row = None
        self.target_shape = None

    def reset_upper_left_position(self, shape: ShapeBase):
        self.upper_left_col = self.WIDTH//2 - shape.width//2
        self.upper_left_row = 0

    def _init_board(self):
        self.board = np.zeros((self.HEIGHT, self.WIDTH))

    def is_full(self, row: int) -> bool:
        return np.all(self.board[row, :] == 1)

    def _set_pre_board(self):
        self.pre_board = self.board.copy()

    def set(self, row: int, col: int):
        self._set_pre_board()
        self.board[row, col] = 1

    def can_move(self, shape: ShapeBase, upper_left_row: int, upper_left_col: int) -> bool:
        # Check relation between shape and edge
        # Col direction
        # check whether shape and left vertical edge is crossed
        if upper_left_col < 0:
            return False

        # check whether shape and right vertical edge is crossed
        can_move_col = shape.width + upper_left_col < self.WIDTH
        if not can_move_col:
            return False

        # Row direction
        # check whether shape and bottom horizontal edge is crossed 
        can_move_row = shape.height + upper_left_row < self.HEIGHT
        if not can_move_row:
            return False

        # Check relation between shape and exist blocks
        target_area = self.board[upper_left_row: upper_left_row+shape.height,
                                 upper_left_col: upper_left_col+shape.width]
        if any(target_area == 1):
            return False

        return True

    def set_target_shape(self, shape: ShapeBase):
        self.target_shape = shape

    def set_shape(self, shape: ShapeBase, upper_left_row: int, upper_left_col):
        self._set_pre_board()
        self.board[upper_left_row: upper_left_row+shape.height,
                   upper_left_col: upper_left_col+shape.width] = 1

    def clear(self, row: int, col: int):
        self.board[row, col] = 0


board = Board()
print(board.board)
shape = OShape()
board.set_shape(shape, 1, 1)
print(board.board)
