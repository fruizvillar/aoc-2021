from __future__ import annotations

from abc import ABC
from datetime import datetime
from enum import Enum
from pathlib import Path
from typing import List

INPUTS = Path.home() / 'PycharmProjects' / 'aoc-2021' / 'inputs'


class Puzzle(ABC):
    N = NotImplemented

    Test = True

    LineType = str

    @classmethod
    def get_inputs(cls) -> List[LineType]:
        test_str = '_test' if cls.Test else ''
        return list(cls.parse_file(INPUTS / f'day_{cls.N:02}{test_str}.txt'))

    @classmethod
    def parse_file(cls, f):
        with f.open() as f_in:
            yield from (cls.LineType(line.strip()) for line in f_in.readlines())

    def __init__(self):
        self.inputs = list(self.get_inputs())  # type: List[Puzzle.LineType]

    def __call__(self, *args, **kwargs):
        t0 = datetime.now()
        self.solve(*args, **kwargs)
        print(f'Took {datetime.now() - t0}')

    def solve(self, *args, **kwargs):
        raise NotImplementedError


class Coordinates:
    """ X, Y coordinates """

    def __init__(self, x=0, y=0):
        self.x = int(x)
        self.y = int(y)

    @property
    def depth(self):
        return -self.y

    def __add__(self, other):
        return Coordinates(self.x + other.x, self.y + other.y)

    def __mul__(self, other):
        return Coordinates(self.x * other, self.y * other)

    def __sub__(self, other):
        return Coordinates(self.x - other.x, self.y - other.y)

    def __abs__(self):
        return (self.x ** 2 + self.y ** 2) ** .5

    def __truediv__(self, other):
        return self.__mul__(1. / other)

    def __str__(self):
        return f'C(x={self.x:3}, y={self.y:3})'

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return self.x * 39 + self.y

    def __iter__(self):
        yield from [self.x, self.y]


class Direction(Enum):
    FORWARD = Coordinates(1)
    DOWN = Coordinates(y=-1)
    UP = Coordinates(y=1)
