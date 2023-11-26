from hp import HP


class Player:
    def __init__(self, max_hp: int) -> None:
        if not isinstance(max_hp, int):
            raise Exception
        self.hp = HP(max=max_hp)

        # reload
        self.__is_reloading: bool = False
        self.__reload_progress: float = 0
        self.__reload_time: float

        # movement
        self.__base_speed: float = 5.0
        self.__reduction_ratio: float = 5.0
        self.__shooting_speed: float = 5.0

    def is_reloading(self) -> bool:
        return self.__is_reloading

    def reload_progress(self) -> float:
        return self.__reload_progress
