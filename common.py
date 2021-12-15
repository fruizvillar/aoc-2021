from abc import ABC
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
            yield from (cls.LineType(line) for line in f_in.readlines())

    def __init__(self):
        self.inputs = list(self.get_inputs())

    def __call__(self, *args, **kwargs):
        self.solve(*args, **kwargs)

    def solve(self, *args, **kwargs):
        raise NotImplementedError
