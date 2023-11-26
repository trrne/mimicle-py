from pg.mathf import Math
from pg.vec2 import V2
from hp import HP


class PlayerRocketLauncher:
    def __init__(self) -> None:
        self.__direction: V2
        self.__base_speed: float = 15.0
        self.__reduction_ratio: float = 0.2
        self.__DAMAGE_RANGE: float = 5.0
        self.__DAMAGE_BASE: float = 25.0
        self.__DAMAGE_MULT: float = 5.0

    def update(self) -> None:
        if self.__base_speed >= 0:
            self.__base_speed -= self.__reduction_ratio
            # movement
            return
        self.__explosion()

    def __explosion(self):
        if closers := self.__closers() is None:
            # generate vfx
            return
        for e in closers:
            distance: float = self.__DAMAGE_RANGE - \
                V2.distance(e.transform.position, transform.position)
            amount: int = Math.cutail(
                distance * self.__DAMAGE_BASE * self.__DAMAGE_MULT)
            e.HP.damage(Math.clamp(amount, 1, 500))

    def __closers(self):  # -> list[GameObject]
        pass
        # enemies: list
        # if enemies is None or len(enemies) <= 0:
        #     return None
        # var closers =
        #     from enemy in enemies
        #     where V2.distance(enemy.transform.position, transform.position) < self.__DAMAGE_RANGE
        #     where enemy.GetComponent<HP>()
        #     select enemy
        # return closers.ToArray()
