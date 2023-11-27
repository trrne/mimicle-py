import dataclasses
from typing import Any
import numpy as np


@dataclasses.dataclass
class V2:
    x: float
    y: float

    def to_tuple(self) -> tuple[int | float, int | float]:
        return (self.x, self.y)

    def to_string(self) -> str:
        return f'{self.x},{self.y}'

    @staticmethod
    def to_v2(t: tuple[int | float, int | float]) -> Any:
        return V2(t[0], t[1])

    def __pos__(self) -> Any:
        return V2(+self.x, +self.y)

    def __neg__(self) -> Any:
        return V2(-self.x, -self.y)

    def __add__(self, other) -> Any:
        if isinstance(other, V2):
            return V2(self.x + other.x, self.y + other.y)
        raise TypeError

    def __sub__(self, other) -> Any:
        if isinstance(other, V2):
            return V2(self.x - other.x, self.y - other.y)
        raise TypeError

    def __mul__(self, other) -> float | Any:
        if isinstance(other, V2):  # cross
            return self.x * other.y - self.y * other.x
        elif isinstance(other, (float, int)):  # scalar
            return self.x * other + self.y * other
        raise TypeError

    def __truediv__(self, other) -> Any:
        if isinstance(other, (int, float)):
            return V2(self.x / other, self.y / other)
        if isinstance(other, V2):
            return V2(self.x / other.x, self.y / other.y)
        raise TypeError

    def __radd__(self, other) -> Any:
        if isinstance(other, V2):
            return V2(other.x + self.x, other.y + self.y)
        raise TypeError

    def __rsub__(self, other) -> Any:
        if isinstance(other, V2):
            return V2(other.x - self.x, other.y - self.y)
        raise TypeError

    def __str__(self) -> str:
        return f'({self.x},{self.y})'

    def magnitude(self) -> float:
        return np.sqrt(self.x**2 + self.y**2)

    @staticmethod
    def cross(a, b) -> Any:
        return a * b

    @staticmethod
    def dot(a, b) -> int | float:
        return a.x * b.x + a.y * b.y

    @staticmethod
    def distance(a, b) -> float:
        if isinstance(a, V2) and isinstance(b, V2):
            return np.round(np.sqrt(np.power(a.x - b.x, 2) + np.power(a.y - b.y, 2)), 3)
        raise TypeError

    @staticmethod
    def min(a, b) -> Any:
        if isinstance(a, V2) and isinstance(b, V2):
            return V2(np.min(a.x, b.x), np.min(a.y, b.y))
        raise TypeError

    @staticmethod
    def max(a, b) -> Any:
        if isinstance(a, V2) and isinstance(b, V2):
            return V2(np.max(a.x, b.x), np.max(a.y, b.y))
        raise TypeError

    @staticmethod
    def angle(a, b) -> float:
        if isinstance(a, V2) and isinstance(b, V2):
            ma: float = a.magnitude()
            mb: float = b.magnitude()
            if np.abs(ma) <= 1e-45 or np.abs(mb) <= 1e-45:
                return 0
            return np.arccos(V2.dot(a, b) / ma / mb) * (180 / np.pi)
        raise TypeError


ZERO = V2(0, 0)
ONE = V2(1, 1)
X = V2(1, 0)
Y = V2(0, 1)
