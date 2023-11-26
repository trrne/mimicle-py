import random


class Random:
    # ? 乱数の仕組み https://qiita.com/mk668a/items/d53515817c41e22e77f0
    # ? 文字列を数値に変換 https://www.hanachiru-blog.com/entry/2019/02/01/190918
    __normal_chars: str = 'abcdefghijklmnopqrstuvwxyz1234567890'
    __jp_chars: str = 'あいうえおかきくけこがぎぐげごさしすせそざじずぜぞたちつてとだぢづでどなにぬねのはひふへほばびぶべぼぱぴぷぺぽまみむめもやゆよらりるれろわをん'

    @staticmethod
    def normal_char(n: int) -> list:
        '''__normal_charsからn個ランダムに取り出す'''
        chars = list(Random.__normal_chars)
        ls: list = []
        for _ in range(n := len(chars)-1 if n > len(chars) else n-1):
            ls.append(chars[Random().randint(0, n)])
        return ls

    @staticmethod
    def jp_char() -> list[str]:
        chars = list(Random.__jp_chars)
        return chars

    @staticmethod
    def mixed_char() -> str:
        return Random.__normal_chars + Random.__jp_chars

    @staticmethod
    def randint(min: int = 0, max: int = 0) -> int:
        return random.SystemRandom().randint(int(min), int(max))

    @staticmethod
    def randfloat(min: float = 0, max: float = 0) -> float:
        return random.SystemRandom().uniform(min, max)

    @staticmethod
    def test_gen(min, max, n) -> tuple[list, list]:
        old: list[int] = []
        new: list[int] = []
        for _ in range(n):
            old.append(random.randint(min, max))
            new.append(Random.randint(min, max))
        return (old, new)
