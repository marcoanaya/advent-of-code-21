from typing import Any, Callable, Optional

class FileUtil:
    @staticmethod
    def file_to_list(
        file_name: str, f: Callable[[str], Any]=lambda x: x, delim: Optional[str]='\n'
    ) -> list[Any]:
        return [f(line.rstrip()) for line in FileUtil.get_file_lines(file_name, delim)]

    @staticmethod
    def get_file_lines(file_name: str, delim: Optional[str]="") -> list[str]:
        with open(file_name, 'r', encoding='utf-8') as file:
            return file.read().strip().split(delim) if delim != "" else file.readlines()
