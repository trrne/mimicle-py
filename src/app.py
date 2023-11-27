import sys
import pygame
from pygame import Surface, display
from pygame.locals import *

from config import *
from trrne.v2 import V2


class app:
    def __init__(self, title: str,  size: V2) -> None:
        self.__title: str = title
        self.__size: V2 = size

    def title(self) -> str:
        return self.__title

    def size(self) -> V2:
        return self.__size

    def screen(self) -> Surface:
        pygame.init()
        display.set_caption(self.title())
        return display.set_mode((self.__size.x, self.__size.y))

    def center(self) -> tuple[int | float, int | float]:
        return (self.__size.x/2, self.__size.y/2)

    @staticmethod
    def font(size: int, is_bold: bool = False, name: str = None) -> pygame.font.SysFont:
        return pygame.font.SysFont(name=name, size=size, bold=is_bold)

    @staticmethod
    def quit() -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or pygame.key.get_pressed()[K_ESCAPE]:
                pygame.quit()
                sys.exit()

    @staticmethod
    def update() -> bool:
        display.update()
        app.quit()
        return sys.executable

    @staticmethod
    def delta_time() -> float:
        return pygame.time.Clock().tick(GAME_FPS) / 1000

    @staticmethod
    def cursor_pos() -> V2:
        return V2(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
