from random import choice
import numpy as np
from typing import Tuple


class ShapeBase:
    def rotate(self):
        self.shape = np.rot90(self.shape)

    @property
    def width(self):
        return self.shape.shape[1]

    @property
    def height(self):
        return self.shape.shape[0]


class IShape(ShapeBase):
    def __init__(self):
        self.shape = np.array(
            [[1],
             [1],
             [1],
             [1]]
        )


class JShape(ShapeBase):
    def __init__(self):
        self.shape = np.array(
            [[0, 1],
             [0, 1],
             [1, 1]]
        )


class LShape(ShapeBase):
    def __init__(self):
        self.shape = np.array(
            [[1, 0],
             [1, 0],
             [1, 1]]
        )


class OShape(ShapeBase):
    def __init__(self):
        self.shape = np.array(
            [[1, 1],
             [1, 1]]
        )


class SShape(ShapeBase):
    def __init__(self):
        self.shape = np.array(
            [[0, 1, 1],
             [1, 1, 0]]
        )


class TShape(ShapeBase):
    def __init__(self):
        self.shape = np.array(
            [[1, 1, 1],
             [0, 1, 0]]
        )


class ZShape(ShapeBase):
    def __init__(self):
        self.shape = np.array(
            [[1, 1, 0],
             [0, 1, 1]]
        )


SHAPES = [
    IShape, JShape, LShape, OShape, SShape, TShape, ZShape
]


def get_shape():
    return choice(SHAPES)
