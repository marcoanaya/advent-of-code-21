from collections import defaultdict
from typing import Any, Callable, DefaultDict, Iterable


class Graph:
    def __init__(self, iterable: Iterable[tuple]) -> None:
        self.edges = DefaultDict(list)
        for k, v in iterable:
            self.edges[k].append(v)
            self.edges[v].append(k)

    def __str__(self) -> str:
        return str(self.edges)

    def find_paths(self, start: Any, end: Any, is_seen:Callable[[Any, Any], bool]) -> list[tuple[Any,...]]:
        paths: list[tuple[Any,...]] = list()
        def dfs(path: list[Any], counts:DefaultDict[Any, int])->None:
            node = path[-1]
            if node == end:
                paths.append(tuple(path))
                return
            for neighbor in self.edges[node]:
                if not is_seen(counts, neighbor):
                    path.append(neighbor)
                    counts[neighbor] += 1
                    dfs(path, counts)
                    del path[-1]
                    counts[neighbor] -= 1
        dfs([start], defaultdict(int, {start: 1}))
        return paths
