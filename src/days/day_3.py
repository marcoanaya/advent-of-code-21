from collections import Counter
from typing import Callable
from .abstract_day import AbstractDay
from ..util.file_util import FileUtil

invert_binary: Callable[[str], str] = lambda x: ''.join('0' if b == '1' else '1' for b in list(x))

class Day3(AbstractDay):
    @staticmethod
    def input(file_name: str) -> list[str]:
        return FileUtil.file_to_list(file_name)
    @staticmethod
    def one(data: list[str]) -> int:
        gamma_lst = len(data[0]) * [0]
        for d in data:
            for i, c in enumerate(d):
                gamma_lst[i] += int(c)
        gamma = ''.join(str(int(x > len(data)/2)) for x in gamma_lst)
        epsilon = invert_binary(gamma)
        return  int(gamma,2) * int(epsilon,2)

    @staticmethod
    def two(data: list[str]) -> int:
        def number_searcher(diag: list[str], most_common: bool, i:int=0) -> str:
            if len(diag) == 1:
                return diag[0]
            count = Counter([x[i] for x in diag]).most_common()
            bit = (
                str(int(most_common))
                if (count[0][1] == count[1][1])
                else count[int(most_common)-1][0]
            )
            diag = list(filter(lambda x: x[i] == bit, diag))
            return number_searcher(diag, most_common, i=i+1)

        oxygen_gen = number_searcher(data, True)
        cee_oh_two = number_searcher(data, False)
        return int(oxygen_gen, 2) * int(cee_oh_two, 2)
