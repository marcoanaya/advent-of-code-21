from typing import Any, DefaultDict
from .abstract_day import AbstractDay
from ..util.file_util import FileUtil
from ..util.graph import Graph

class Day12(AbstractDay):
    @classmethod
    def input(cls, file_name: str) -> Any:
        return Graph(FileUtil.file_to_list(file_name, f=lambda x: x.split('-')))

    @classmethod
    def one(cls, caves: Any) -> int:
        v = caves.find_paths('start', 'end', is_seen=lambda counts, node: counts[node] >= 1  and node.islower())
        return len(v)

    @classmethod
    def two(cls, caves: Any) -> int:
        def is_seen(counts: DefaultDict[Any, int], node: Any) -> bool:
            return  (
                node.islower() and counts[node] >= 1
                and (node in ['start', 'end'] or any(v >= 2 for k, v in counts.items() if k.islower()))
            )
        v = caves.find_paths('start', 'end', is_seen)
        return len(v)
