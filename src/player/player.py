import pygame
from pygame.locals import *

from hp import HP
from trrne.vec2 import V2


class Player:
    def __init__(
        self,
        screen: pygame.Surface,
        image: pygame.Surface,
        max_hp: int,
        pos: V2,
        speed: float
    ) -> None:
        self.__controllable = True

        self.__hp: HP = HP(max=max_hp)
        self.__pos: V2 = pos

        self.__screen: pygame.Surface = screen
        self.__image: pygame.Surface = image

        # reload
        self.__is_reloading: bool = False
        self.__reload_progress: float = 0
        self.__reload_time: float

        # movement
        self.__speed: float = speed
        self.__reduction_ratio: float = 5.0
        self.__shooting_speed: float = 5.0

    def hp(self) -> HP:
        return self.__hp

    def render(self) -> None:
        self.__screen.blit(self.__image, self.pos.to_tuple())

    def update(self, dt: float) -> None:
        if not self.__controllable:
            return
        if not (key_pressed := pygame.key.get_pressed()):
            self.__speed.x *= self.__reduction_ratio
            self.__speed.y *= self.__reduction_ratio
            return
        if key_pressed[K_w]:
            self.__pos.y -= dt*self.__speed
        if key_pressed[K_s]:
            self.__pos.y += dt*self.__speed
        if key_pressed[K_a]:
            self.__pos.x -= dt*self.__speed
        if key_pressed[K_d]:
            self.__pos.x += dt*self.__speed

    @property
    def controllable(self) -> bool:
        return self.__controllable

    @controllable.setter
    def controllable(self, boo: bool) -> None:
        self.__controllable = boo

    @property
    def speed(self) -> float:
        return self.__speed

    @speed.setter
    def speed(self, new_speed: float) -> None:
        self.__speed = new_speed

    @property
    def pos(self) -> V2:
        return self.__pos

    @pos.setter
    def pos(self, pos: V2) -> None:
        self.__pos = pos

    def is_reloading(self) -> bool:
        return self.__is_reloading

    def reload_progress(self) -> float:
        return self.__reload_progress

    @property
    def reload_time(self) -> float:
        return self.__reload_time

    @reload_time.setter
    def reload_time(self, time: float) -> None:
        self.__reload_time = time
