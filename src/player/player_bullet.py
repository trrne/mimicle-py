from pg.vec2 import V2


class PlayerBullet:
    def __init__(self) -> None:
        self.__direction: V2
        self.__SPEED: float = 20.0

    def move(self, speed: float) -> None:
        pass

    # def take_damage(self):
    #     pass
