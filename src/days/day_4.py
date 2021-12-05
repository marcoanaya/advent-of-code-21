from .abstract_day import AbstractDay
from ..util.file_util import FileUtil

invert_binary = lambda x: ''.join('0' if b == '1' else '1' for b in list(x))

class Board:
    def __init__(self, board_str: str):
        rows = [list(map(int,row.split())) for row in board_str.split('\n')]
        cols: list[list[int]] = list(map(list, zip(*rows)))
        self.sum = sum(sum(row) for row in rows)
        self.options = rows + cols
        self.left = len(self.options) * [5]
        self.marked: list[int] = []
        self.won = 0

    def draw(self, num:int) -> int:
        if self.won:
            return self.get_score(self.won)
        added = False
        for i, option in enumerate(self.options):
            if num in option:
                if not added:
                    self.marked.append(num)
                    added = True
                self.left[i] -= 1
                if self.left[i] == 0:
                    self.won = num
        return self.get_score(num)

    def get_score(self, num: int) -> int:
        if all(self.left):
            return 0
        return (self.sum - sum(self.marked)) * num

class Day4(AbstractDay):
    @staticmethod
    def one() -> int:
        numbers, board_strs = FileUtil.file_to_numbers_and_boards(Day4.get_file_name())

        boards = list(map(Board, board_strs))
        for num in numbers:
            winner = [w for w in list(b.draw(num) for b in boards) if w]
            if winner:
                return winner[0]
        return -1

    @staticmethod
    def two() -> int:
        numbers, board_strs = FileUtil.file_to_numbers_and_boards(Day4.get_file_name())

        boards = list(map(Board, board_strs))
        for num in numbers:
            losers = [b for b in boards if b.draw(num) == 0]
            if len(losers) == 1:
                for rem_num in numbers[numbers.index(num)+1:]:
                    if losers[0].draw(rem_num):
                        return losers[0].get_score(rem_num)
        return -1
