from typing import Generic, TypeVar
import random

TItem = TypeVar('TItem')


class LotteryPair(Generic[TItem]):
    def __init__(self, pairs: list[tuple[TItem, float]]) -> None:
        super().__init__()
        self.pairs: list[tuple[TItem, float]] = pairs
        self.items: list[TItem] = []
        self.weights: list[float] = []
        for i in range(len(pairs)):
            self.items.append(pairs[i][0])
            self.weights.append(pairs[i][1])

    def size(self) -> int:
        return len(self.pairs)


class Lottery(Generic[TItem]):
    @staticmethod
    def binary_search_tree(weights: list[float]) -> int:
        '''二分探索木'''
        if len(weights) <= 0:
            raise Exception('からっぽやんけ')

        totals: list[float] = []
        total: float = 0.0
        for i in range(len(weights)):
            total += weights[i]
            totals.append(total)

        rnd: float = random.uniform(0, total)
        bottom: int = 0
        top: int = len(totals)-1
        while bottom < top:
            center: int = int((bottom+top)/2)
            if rnd > totals[center]:
                bottom = center+1
            else:
                if rnd >= totals[center-1] if center > 0 else 0.0:
                    return center
                top = center
        return top

    @staticmethod
    def weighted(pairs: LotteryPair[TItem]) -> TItem:
        if pairs.size() <= 0:
            raise Exception()
        return pairs.items[Lottery.binary_search_tree(pairs.weights)] if pairs.size() != 1 else pairs.items[0]
