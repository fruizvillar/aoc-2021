from common import Puzzle, Coordinates, Direction


class DailyPuzzle(Puzzle):
    N = 2

    Test = False

    Aim = 0

    def solve(self, *args, **kwargs):
        typed_inputs = [(x, int(y)) for x, y in [z.split() for z in self.inputs]]
        print(*typed_inputs)

        pos = Coordinates()

        print(pos)
        for movement in typed_inputs:
            pos += self._parse_mov(*movement)
            print(pos)

        pos = Coordinates()

        print('PART 2')
        for movement in typed_inputs:
            pos += self._parse_aimed_mov(*movement)
            print(pos)

    def _parse_aimed_mov(self, direction, amount):
        if direction == 'forward':

            val = Direction.FORWARD.value * amount
            val += Direction.DOWN.value * self.Aim * amount

            return val

        elif direction == 'down':
            self.Aim += amount
        else:
            self.Aim -= amount

        return Coordinates()  # We don't move so we return 0

    @staticmethod
    def _parse_mov(direction, amount):
        val = Direction[direction.upper()].value * amount
        return val


if __name__ == '__main__':
    DailyPuzzle()()
