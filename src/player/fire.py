from ammo import Ammo


class Fire:
    def __init__(self, ammo: Ammo) -> None:
        self.__ammo: Ammo = ammo
        self.__mode: int = 0
        self.__grade: int = 0
        self.__is_firing: bool = False

    def mode(self) -> int:
        return self.__mode

    def grade(self) -> int:
        return self.__grade

    def is_firing(self) -> bool:
        return self.__is_firing

    def change_weapon(self) -> None:
        pass

    def shot(self, active_grade: int):
        if not isinstance(active_grade, int):
            raise Exception
        self.__is_firing = True
        self.__grade = active_grade
        self.__ammo.reduce()
        if active_grade == (0 or 1):
            print('shot AR')
        else:
            print('shot RL')
            pass
