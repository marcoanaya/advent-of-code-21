from .abstract_day import AbstractDay
from ..util.file_util import FileUtil

class Day20(AbstractDay):
    @classmethod
    def input(cls, file_name: str) -> tuple['ImageEnhancementAlgorithm', 'Image']:
        algorithm, _, *input_image =  FileUtil.file_to_list(file_name)
        return ImageEnhancementAlgorithm(algorithm), Image(input_image)

    @classmethod
    def one(cls, data: tuple['ImageEnhancementAlgorithm', 'Image']) -> int:
        algorithm, img = data
        for _ in range(2):
            img = algorithm.enhance(img)
        return img.count_lit_pixels()

    @classmethod
    def two(cls, data: tuple['ImageEnhancementAlgorithm', 'Image']) -> int:
        algorithm, img = data
        for _ in range(50):
            img = algorithm.enhance(img)
        return img.count_lit_pixels()

class Image(list):
    def __init__(self, img: list[str], fill: str='.', margin: int=2) -> None:
        empty_rows = [fill * (len(img[0]) + (2*margin)) for _ in range(margin)]
        super().__init__([
            *empty_rows,
            *[f"{fill*margin}{s}{fill*margin}" for s in img],
            *empty_rows
        ])
        self.fill = fill

    def count_lit_pixels(self) -> int:
        return sum(int(c == '#') for row in self for c in row)

    def __str__(self) -> str:
        return '\n'.join(self)

    __repr__ = __str__

class ImageEnhancementAlgorithm:
    def __init__(self, s: str) -> None:
        self.s = s
        self.start_char = s[0]
        self.end_char = s[-1]

    def get_pixel(self, nine_pixels: list[str]) -> str:
        return self.s[int(''.join(str(int(c == '#')) for c in ''.join(nine_pixels)), 2)]

    def enhance(self, img: 'Image') -> 'Image':
        return Image([
                ''.join(self.get_pixel([img[k][j-1:j+2] for k in range(i-1, i+2)]) for j in range(1, len(img[i])-1))
                for i in range(1, len(img)-1)
            ],
            fill='.' if (img.fill == '.' == self.start_char) or (img.fill == '#' != self.end_char) else '#'
        )
