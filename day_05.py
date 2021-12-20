import re
from collections import defaultdict
from typing import List

from common import Puzzle, Coordinates


class VentLine:
    Regex = re.compile(r'(\d+),(\d+) -> (\d+),(\d+)')

    def __init__(self, line):
        match = self.Regex.match(line).groups()
        self.orig = Coordinates(*match[:2])
        self.dest = Coordinates(*match[2:])

    @property
    def directions(self):
        dir_not_norm = self.dest - self.orig
        dir_x = dir_not_norm.x / abs(dir_not_norm.x) if dir_not_norm.x else 0
        dir_y = dir_not_norm.y / abs(dir_not_norm.y) if dir_not_norm.y else 0
        return Coordinates(dir_x, dir_y)

    @property
    def is_hor_or_vert(self):
        return self.is_horizontal or self.is_vertical

    @property
    def is_diagonal(self):
        return not (self.is_horizontal or self.is_vertical)

    @property
    def is_vertical(self):
        return not self.directions.x

    @property
    def is_horizontal(self):
        return not self.directions.y

    def get_points(self):

        length = max(abs(x) for x in (self.dest-self.orig))
        for i in range(length + 1):
            p = self.orig + self.directions * i
            yield self.orig + self.directions * i


    def __str__(self):
        return f'L( {self.orig} -> {self.dest} ){" H" if self.is_horizontal else ""}' \
               f'{" V" if self.is_vertical else ""}{"  " if self.is_diagonal else ""}'


class DailyPuzzle(Puzzle):
    N = 5

    Test = False

    LineType = VentLine

    Threshold = 2

    def solve(self, *args, **kwargs):
        print('Part 1')

        lines_hv = [line for line in self.inputs if not line.is_diagonal]  # type: List[VentLine]
        print(f'# H/Vlines: {len(lines_hv)}')

        n = self.get_n_lines_above_thr(lines_hv)
        print('N points above THR', n)

        print('Part 2')
        print(f'# lines: {len(self.inputs)}')

        n = self.get_n_lines_above_thr(self.inputs)
        print('N points above THR', n)

    def get_n_lines_above_thr(self, lines):
        all_points_noflat = [line.get_points() for line in lines]
        all_points = [item for sublist in all_points_noflat for item in sublist]
        print('# points:', len(all_points))
        unique_points = defaultdict(lambda: 0)
        for p in all_points:
            unique_points[p] += 1

        n = len([k for k, v in unique_points.items() if v >= self.Threshold])
        return n


if __name__ == '__main__':
    DailyPuzzle()()
