class Game:
    def __init__(self):
        self._rolls = []

    def roll(self, pins):
        self._rolls.append(pins)

    def score(self):
        total = 0
        roll_index = 0
        for _ in range(10):
            if self._is_strike(roll_index):
                total += 10 + self._strike_bonus(roll_index)
                roll_index += 1
            elif self._is_spare(roll_index):
                total += 10 + self._rolls[roll_index + 2]
                roll_index += 2
            else:
                total += self._frame_sum(roll_index)
                roll_index += 2
        return total

    def _is_strike(self, roll_index):
        return self._rolls[roll_index] == 10

    def _strike_bonus(self, roll_index):
        return self._rolls[roll_index + 1] + self._rolls[roll_index + 2]

    def _is_spare(self, roll_index):
        return self._frame_sum(roll_index) == 10

    def _frame_sum(self, roll_index):
        return self._rolls[roll_index] + self._rolls[roll_index + 1]
