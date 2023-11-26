import sys
import pygame
from pygame import Surface, display
from pygame.locals import *

from trrne.res import Resolution
from trrne.colour import COLOR
from trrne.vec2 import V2


class app:
    def __init__(self, title: str,  resolution: Resolution) -> None:
        self.__title: str = title
        self.__resolution: Resolution = resolution

    def title(self) -> str:
        return self.__title

    def resolution(self) -> Resolution:
        return self.__resolution

    # @staticmethod
    def screen(self) -> Surface:
        pygame.init()
        display.set_caption(self.title())
        return display.set_mode((self.resolution().width, self.resolution().height))

    # @staticmethod
    def center(self) -> tuple[int, int]:
        center = self.__resolution.center()
        return (center.x, center.y)

    @staticmethod
    def font(name: str, size: int, is_bold: bool) -> pygame.font.SysFont:
        return pygame.font.SysFont(name=name, size=size, bold=is_bold)

    @staticmethod
    def quit() -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or pygame.key.get_pressed()[K_ESCAPE]:
                pygame.quit()
                sys.exit()

    # @staticmethod
    # def update() -> None:
    #     display.update()
    #     app.quit()

    @staticmethod
    def update() -> bool:
        display.update()
        app.quit()
        return sys.executable  # __is_running
