﻿class Math:
    PI: float = 3.141592653589793
    DEG_TO_RAD: float = PI / 180
    RAD_TO_DEG: float = 180 / PI

    @staticmethod
    def round(n: int | float, digit: int = 1) -> int | float:
        return (n * 10 ** digit * 2 + 1) // 2 / 10 ** digit

    @staticmethod
    def digit(n) -> int:
        return len(str(n).replace('.', ''))

    @staticmethod
    def clamp(target, min=0, max=1) -> int | float:
        return min if target < min else max if target > max else target

    @staticmethod
    def lerp(o, p, time) -> float:
        return o + (p - o) * Math.clamp(time)

    @staticmethod
    def eratosthenes(n: int) -> list[int]:
        ''' nまでの素数を返す '''
        flags: list[bool] = [True] * (n+1)
        flags[0], flags[1] = False, False

        for i in range(2, int(n**0.5)+1):
            if flags[i]:
                for j in range(2*i, n+1, i):
                    flags[j] = False
        return [i for i in range(2, n+1) if flags[i]]

    @staticmethod
    def min(a: float, b: float) -> float:
        return a if a < b else b

    @staticmethod
    def max(a: float, b: float) -> float:
        return a if a > b else b

    @staticmethod
    def pow(n: int | float, a: int) -> int | float:
        if not isinstance(a, int):
            raise Exception()
        return n ** a

    @staticmethod
    def cutail(n: float) -> int:
        return int(str(n).split('.')[0])
