from common import Puzzle


class Day03(Puzzle):
    N = 3

    Test = False

    NumericMode = False

    def __init__(self):
        super().__init__()
        self.n = len(self.inputs)
        self.width = len(self.inputs[0])
        self.gamma_str = None
        self._g = self._e = self._o2 = self._co2 = None

    def solve(self, *args, **kwargs):

        print('PART 1')
        print('Gamma: ', self.gamma_rate)
        print('Epsilon: ', self.epsilon_rate)
        print('Power: ', self.power_consumption)

        print('\nPART 2')
        print('O2 gen: ', self.oxygen_generator_rating)
        print('CO2 scrub: ', self.co2_scrub_rating)
        print('Life support: ', self.life_support_rating)

    @classmethod
    def _most_common_in_pos(cls, v, pos):
        pos_values = [word[pos] for word in v]
        if cls.NumericMode:
            total = sum(int(c) for c in pos_values)
            return str((2 * total) // len(v))

        else:
            t = {'0': 0, '1': 0}

            for c in pos_values:
                t[c] += 1

            return '1' if t['1'] >= t['0'] else '0'

    @property
    def gamma_rate(self):
        if self._g is None:

            gamma = []
            for index in range(self.width):

                gamma.append(self._most_common_in_pos(self.inputs, index))

            self.gamma_str = ''.join(gamma)

            self._g = int(self.gamma_str, 2)
        return self._g

    @property
    def epsilon_rate(self):
        if self._e is None:
            if self.gamma_str is None:
                _ = self.gamma_rate

            epsilon_str = self.gamma_str.replace('0', 'x').replace('1', '0').replace('x', '1')

            self._e = int(epsilon_str, 2)

        return self._e

    @property
    def power_consumption(self):
        return self.gamma_rate * self.epsilon_rate

    @property
    def oxygen_generator_rating(self):
        if self._o2 is None:
            words_in = self.inputs.copy()
            for index in range(self.width):

                most_common = self._most_common_in_pos(words_in, index)

                words_in = list(filter(lambda w: w[index] == most_common, words_in))

                if len(words_in) == 1:
                    break

            self._o2 = int(words_in[0], 2)

        return self._o2

    @property
    def co2_scrub_rating(self):
        if self._co2 is None:
            words_in = self.inputs.copy()
            for index in range(self.width):
                most_common = self._most_common_in_pos(words_in, index)

                words_in = list(filter(lambda w: w[index] != most_common, words_in))

                if len(words_in) == 1:
                    break

            self._co2 = int(words_in[0], 2)

        return self._co2

    @property
    def life_support_rating(self):
        return self.co2_scrub_rating * self.oxygen_generator_rating


if __name__ == '__main__':
    Day03()()
