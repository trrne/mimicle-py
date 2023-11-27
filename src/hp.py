from trrne.mathf import Math


class HP:
    def __init__(self, max: int) -> None:
        if not isinstance(max, int):
            raise Exception
        self.__max: int = max
        self.__now: int = self.__max

    @property
    def max(self) -> int:
        return self.__max

    @max.setter
    def max(self, value: int) -> None:
        if not isinstance(value, int):
            raise Exception
        self.__max = value

    def now(self) -> int:
        return self.__now

    def ratio(self) -> float:
        return float(self.__now) / float(self.__max)

    def reset(self) -> None:
        self.__now = self.__max

    def healing(self, amount: int) -> None:
        if not isinstance(amount, int):
            raise Exception
        self.__now = Math.clamp(self.__now, 0, self.__max)
        self.__now += amount
        if self.__now > self.__max:
            self.__now = self.__max

    def damage(self, amount: int) -> None:
        if not isinstance(amount, int):
            raise Exception
        self.__now = Math.clamp(self.__now, 0, self.__max)
        self.__now -= amount
        if self.__now < 0:
            self.__now = 0
