from .abstract_day import AbstractDay
from ..util.file_util import FileUtil


class Day4(AbstractDay):
    @staticmethod
    def one() -> int:
        numbers, board_rows = FileUtil.file_to_numbers_and_boards(Day4.get_file_name())
        boards = list(map(Day4.Board, board_rows))
        for num in numbers:
            winner = [w for w in list(b.draw(num) for b in boards) if w]
            if winner:
                return winner[0]
        return -1

    @staticmethod
    def two() -> int:
        numbers, board_rows = FileUtil.file_to_numbers_and_boards(Day4.get_file_name())
        boards = list(map(Day4.Board, board_rows))
        for num in numbers:
            losers = [b for b in boards if b.draw(num) == 0]
            if len(losers) == 1:
                for rem_num in numbers[numbers.index(num)+1:]:
                    if losers[0].draw(rem_num):
                        return losers[0].get_score(rem_num)
        return -1

    class Board:
        def __init__(self, rows: list[list[int]]):
            self.options = rows + list(map(list, zip(*rows)))
            self.sum = sum(sum(row) for row in rows)
            self.left = len(self.options) * [5]
            self.marked: set[int] = set()
            self.winning_num = 0

        def draw(self, num:int) -> int:
            if score := self.get_score(self.winning_num):
                return score
            for i, option in enumerate(self.options):
                if num in option:
                    self.marked.add(num)
                    self.left[i] -= 1
                    if not self.left[i]:
                        self.winning_num = num
            return self.get_score(num)

        def get_score(self, num: int) -> int:
            if all(self.left):
                return 0
            return (self.sum - sum(self.marked)) * num
