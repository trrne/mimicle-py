from enum import Enum

from trrne.vec2 import V2


class RESNUM:
    NULL: tuple[int, int] = (0, 0)
    HD: tuple[int, int] = (1280, 720)
    FHD: tuple[int, int] = (1920, 1080)
    WQHD: tuple[int, int] = (2560, 1440)


class Resolution:
    def __init__(self, w: int = 0, h: int = 0, res: RESNUM = RESNUM.NULL) -> None:
        self.__size: V2
        if RESNUM == RESNUM.NULL and w == 0 and h == 0:
            # raise Exception
            self.__size = V2(1280, 720)
        elif RESNUM != RESNUM.NULL:
            self.__size = V2(res[0], res[1])
        elif w != 0 and h != 0:
            self.__size = V2(w, h)
        else:
            raise Exception
    # def __init__(self, res: tuple[int, int]) -> None:
        # print(V2(res[0], res[1]))
        # self.__size = V2(res[0], res[1])

    @property
    def width(self) -> int:
        return int(self.__size.x)

    @width.setter
    def width(self, w: int) -> None:
        self.__size.x = w

    @property
    def height(self) -> int:
        return int(self.__size.y)

    @height.setter
    def height(self, h: int) -> None:
        self.__size.y = h

    def center(self) -> V2:
        return V2(self.__size.x/2, self.__size.y/2)
