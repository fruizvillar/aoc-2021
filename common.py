from abc import ABC
from enum import Enum
from pathlib import Path

INPUTS = Path.home() / 'PycharmProjects' / 'aoc-2021' / 'inputs'


class Puzzle(ABC):
    N = NotImplemented

    Test = True

    LineType = str

    @classmethod
    def get_inputs(cls):
        test_str = '_test' if cls.Test else ''
        return cls.parse_file(INPUTS / f'day_{cls.N:02}{test_str}.txt')

    @classmethod
    def parse_file(cls, f):
        with f.open() as f_in:
            yield from (cls.LineType(line.strip()) for line in f_in.readlines())

    def __init__(self):
        self.inputs = list(self.get_inputs())

    def __call__(self, *args, **kwargs):
        self.solve(*args, **kwargs)

    def solve(self, *args, **kwargs):
        raise NotImplementedError


class Coordinates:
    """ X, Y coordinates """
    def __init__(self, x=0, y=0):
        self.x, self.y = x, y

    @property
    def depth(self):
        return -self.y

    def __add__(self, other):
        return Coordinates(self.x + other.x, self.y + other.y)

    def __mul__(self, other):
        return Coordinates(self.x * other, self.y * other)

    def __str__(self):
        return f'Coordinates (x={self.x}, y={self.y}) (val = {self.depth * self.x})'


class Direction(Enum):
    FORWARD = Coordinates(1)
    DOWN = Coordinates(y=-1)
    UP = Coordinates(y=1)
