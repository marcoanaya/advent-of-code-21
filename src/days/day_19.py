import re
import math
from typing import Generator, Optional
from itertools import combinations
import numpy as np
from numpy.typing import NDArray
from .abstract_day import AbstractDay
from ..util.file_util import FileUtil
from ..util.misc import unwrap

class Day19(AbstractDay):
    @classmethod
    def input(cls, file_name: str) -> 'ScannerContainer':
        return ScannerContainer(FileUtil.file_to_list(file_name, f=Scanner.from_string, delim='\n\n'))

    @classmethod
    def one(cls, data: 'ScannerContainer') -> int:
        return len(data.find_beacons())

    @classmethod
    def two(cls, data: 'ScannerContainer') -> int:
        data.find_beacons()
        positions = [unwrap(s.position) for s in data.scanners]
        return max(np.abs(u - v).sum() for u, v in combinations(positions, 2))

class ScannerContainer:
    def __init__(self, scanners: list['Scanner']) -> None:
        self.scanners = scanners
        self.scanners_found = 1

    def find_beacons(self) -> set[tuple]:
        first, *_ = self.scanners
        beacons: set[tuple[int, ...]] = set(map(tuple, first.beacons))
        first.position = np.array([0, 0, 0])
        while self.scanners_found < len(self.scanners):
            for s1, s2, v in self.get_possible_matches():
                if (s1.position is not None) != (s2.position is not None):
                    if s2.position is not None:
                        s1, s2 = s2, s1
                    beacons |= s2.find_new_beacons_and_update(s1, v)
                    self.scanners_found += 1
        return beacons

    def get_possible_matches(self) -> Generator[tuple['Scanner', 'Scanner', frozenset], None, None]:
        yield from (
            (s1, s2, next(iter(matches)))
            for s1, s2 in combinations(self.scanners, 2)
            if len(matches := set(s1.hash) & set(s2.hash)) >= math.comb(12, 2)
        )

class Scanner:
    directions: list[NDArray] = list(map(np.array, [
        (1, 0, 0),
        (0, 1, 0),
        (0, 0, 1),
        (-1, 0, 0),
        (0, -1, 0),
        (0, 0, -1),
    ]))

    def __init__(self, identifier: int, beacons: NDArray) -> None:
        self.id = identifier
        self.beacons = beacons
        self.hash = {
            frozenset(map(abs, self.beacons[i, :] - self.beacons[j, :])): (i, j)
            for i, j in combinations(range(len(self.beacons)), 2)
        }
        self.position: Optional[NDArray] = None

    def find_new_beacons_and_update(self,  other: 'Scanner', match: frozenset) -> set[tuple]:
        for rotated_beacons in self.get_rotations():
            i = other.hash[match][0]
            for j in self.hash[match]:
                diff = other.beacons[i, :] - rotated_beacons[j, :]
                new_beacons = set(map(tuple, rotated_beacons + diff))
                if len(new_beacons & set(map(tuple, other.beacons))) >= 12:
                    self.beacons = rotated_beacons + diff
                    self.position = diff
                    return new_beacons
        raise Exception('no new beacons found')

    def get_rotations(self) -> Generator[NDArray, None, None]:
        yield from (
            np.matmul(self.beacons, np.array([u, v, np.cross(u, v)]))
            for u in self.directions for v in self.directions
            if u.dot(v) == 0
        )

    @staticmethod
    def from_string(string: str) -> 'Scanner':
        header, *beacon_strs = string.split('\n')
        identifier = int(re.findall(r'\d+', header)[0])
        beacons = np.array([list(map(int,s.split(','))) for s in beacon_strs])
        return Scanner(identifier, beacons)

    def __str__(self) -> str:
        return f"Scanner({self.id},\n{self.beacons})"
    __repr__=__str__
