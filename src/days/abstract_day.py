from abc import ABC, abstractmethod
from typing import Any


class AbstractDay(ABC):
    @classmethod
    def get_number(cls) -> int:
        return int(cls.__name__.strip("Day"))

    @classmethod
    @abstractmethod
    def input(cls, file_name: str) -> Any:
        pass

    @classmethod
    @abstractmethod
    def one(cls, data: Any) -> int:
        pass

    @classmethod
    @abstractmethod
    def two(cls, data: Any) -> int:
        pass
