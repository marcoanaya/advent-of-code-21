import sys
import importlib
import glob
import re
from typing import Type
from src.days.abstract_day import AbstractDay
import src.days


class DayUtil:
    @staticmethod
    def new_day(n: int) -> None:
        with open(f"./src/days/day_{n}.py", "w", encoding="utf-8") as f:
            f.write(f"""from typing import Any
from .abstract_day import AbstractDay
from ..util.file_util import FileUtil

class Day{n}(AbstractDay):
    @staticmethod
    def input(file_name: str) -> Any:
        return FileUtil.file_to_list(file_name)

    @staticmethod
    def one(data: Any) -> int:
        pass

    @staticmethod
    def two(data: Any) -> int:
        pass
""")

    @staticmethod
    def get_days() -> list[Type[AbstractDay]]:
        for file in glob.glob("./src/days/day*.py"):
            match = re.search('./src/days/(.+?).py', file)
            if match:
                importlib.import_module(f"src.days.{match.group(1)}")

        day_modules = [(name, mod) for name, mod in src.days.__dict__.items() if name.startswith('day_')]
        day_modules.sort(key=lambda x: int(x[0].strip('day_')))
        day_modules = list(map(lambda x: x[1], day_modules))
        get_cls = lambda mod: next(cls for name, cls in mod.__dict__.items() if name.startswith('Day'))
        return list(map(get_cls, day_modules))


if __name__ == '__main__':
    num = int(sys.argv[1])
    DayUtil.new_day(num)
