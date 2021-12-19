from common import Puzzle


class DailyPuzzle(Puzzle):
    N = 4

    Test = False

    def __init__(self):
        super(DailyPuzzle, self).__init__()

        self._read_bingo()

    def solve(self, *args, **kwargs):
        self._print_bingo()
        n = None
        b_win = None

        for i, n in enumerate(self.random_pick):
            print(f'Round = {i}. Marking {n}.')

            for b in self.boards:
                b.mark(n)

                if b.has_line:
                    b_win = b

            self._print_bingo()

            if b_win is not None:
                break

        print(f'Line found! {n=}')

        if b_win:
            print(f'Score = {b_win.points * n}')


        print('PART TWO!')
        self._clear()

        n = None
        b_ranking = []

        for i, n in enumerate(self.random_pick):
            print(f'Round = {i}. Marking {n}.')

            for b in self.boards:
                b.mark(n)

                if b not in b_ranking and b.has_line:
                    b_ranking.append(b)

            self._print_bingo()

            if all(b.has_line for b in self.boards):
                break

        print(f'Line found for all! {n=}')

        b_lost = b_ranking[-1]
        print(f'Score of last = {b_lost.points * n}')

    def _read_bingo(self):
        self.random_pick = [int(x) for x in self.inputs[0].split(',')]

        self.boards = []

        n_row = 2  # 1st: random pick, 2nd: space
        a_board = []

        try:
            while True:
                if next_row := [int(x) for x in self.inputs[n_row].split()]:
                    a_board.append(next_row)

                else:
                    self.boards.append(Board(a_board))
                    a_board = []

                n_row += 1
        except IndexError:
            self.boards.append(Board(a_board))

    def _print_bingo(self):
        for board in self.boards:
            print(board)

    def _clear(self):
        for board in self.boards:
            board.clear()

class Board:

    def __init__(self, array, n=None):
        self.array = array
        self.width = len(array)
        self.n = n
        self.marked = None
        self.clear()

    def mark(self, n):
        for y, row in enumerate(self.array):
            for x, value in enumerate(row):
                if n == value:
                    self.marked[y][x] = True

    @property
    def has_line(self):
        return self.has_row or self.has_col

    @property
    def has_row(self):
        return any([all(line) for line in self.marked])

    @property
    def has_col(self):
        return any([all([line[j] for line in self.marked]) for j in range(self.width)])

    @property
    def points(self):
        acc = 0
        for y, line in enumerate(self.array):
            for x, value in enumerate(line):
                if not self.marked[y][x]:
                    acc += value
        return acc

    def clear(self):
        self.marked = [[False] * self.width for _ in range(self.width)]

    def __str__(self):
        ret = '┌' + '─' * (self.width * 5 - 1) + '┐\n'
        for y, line in enumerate(self.array):
            vs = []
            for x, value in enumerate(line):
                vs.append(f'[{value:2d}]' if self.marked[y][x] else f' {value:2d} ')
            ret += '│' + ' '.join(vs) + '│\n'

        ret += '└' + '─' * (self.width * 5 - 1) + '┘'

        if self.has_row:
            ret += ' → ROW'
        if self.has_col:
            ret += ' → COL'

        return ret


if __name__ == '__main__':
    DailyPuzzle()()
