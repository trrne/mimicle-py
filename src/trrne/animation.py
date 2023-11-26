import dataclasses


@dataclasses.dataclass
class Animation:
    total_count: int
    seconds: float

    def now_count(self) -> int:
        return self.seconds % self.total_count
