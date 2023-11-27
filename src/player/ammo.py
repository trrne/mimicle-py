from trrne.mathf import Math


class Ammo:
    def __init__(self, max: int) -> None:
        if not isinstance(max, int):
            raise Exception
        self.__max = max
        self.__remain = self.__max

    def remain(self) -> int:
        return self.__remain

    @property
    def max(self) -> int:
        return self.__max

    @max.setter
    def max(self, value: int) -> None:
        if not isinstance(value, int):
            raise Exception
        self.__max = value

    def ratio(self) -> float:
        return float(self.__remain) / float(self.__max)

    def is_max(self) -> bool:
        return self.__remain >= self.__max

    def reduce(self, amount: int) -> None:
        if not isinstance(amount, int):
            raise Exception
        self.__remain -= amount
        if self.__remain < 0:
            self.__remain = 0

    def reload(self) -> None:
        if self.is_max():
            return
        for _ in range(0, self.__max, 1):
            self.__remain = Math.clamp(self.__remain, 0, self.__max)
            self.__remain += 1
        if self.__remain > self.__max:
            self.__remain = self.__max
