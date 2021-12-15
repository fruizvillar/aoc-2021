from common import Puzzle


class Day01(Puzzle):
    N = 1
    LineType = int

    Test = False

    def solve(self, *args, **kwargs):
        print('Inputs: ', self.inputs)

        print('\nPART ONE\n')
        averaged = self.moving_average(w=1)
        print('Averaged: ', averaged)
        self.get_n_increases(averaged)

        print('\nPART TWO\n')

        averaged = self.moving_average(w=3)
        print('Averaged: ', averaged)
        self.get_n_increases(averaged)

    def moving_average(self, w):
        vectors = []
        for i_0 in range(w):

            if i_f := - (w - i_0 - 1):
                v = self.inputs[i_0:i_f]
            else:
                v = self.inputs
            vectors.append(v)

        return [sum(vi) for vi in zip(*vectors)]

    @staticmethod
    def get_n_increases(averaged):
        diff = [x - y for x, y in zip(averaged[1:], averaged[:-1])]
        print('Diff: ', diff)

        incr = [x > 0 for x in diff]
        print('Incr: ', incr)

        print('# incr.: ', sum(incr))


if __name__ == '__main__':
    Day01()()
