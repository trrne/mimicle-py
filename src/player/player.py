import os
import pygame
from pygame.locals import *

from hp import HP
from player.ammo import Ammo
from player.gun import Gun
from trrne.v2 import V2
from config import *


class Player:
    def __init__(
        self,
        screen: pygame.Surface,
        # image: pygame.Surface,
        max_hp: int,
        pos: V2,
        speed: float
    ) -> None:
        self.__ctrlable = True

        self.__hp: HP = HP(max=max_hp)
        self.__pos: V2 = pos
        self.__screen: pygame.Surface = screen
        self.__image: pygame.Surface = self.load_sprite()
        self.__is_reloading: bool = False
        self.__reload_progress: float = 0
        self.__reload_time: float
        self.__speed: float = speed
        self.__reduction_ratio: float = 5.0
        self.__shooting_speed: float = 5.0
        self.__ammo = Ammo()
        self.__gun = Gun(ammo=self._ammo)
        self.__grade = 0

    def load_sprite(self) -> pygame.Surface:
        player_image: pygame.Surface = pygame.image.load(
            os.path.join(PLAYER_PATH_PREFIX, PLAYER_NAME))
        player_image_xflipped: pygame.Surface = pygame.transform.flip(
            player_image, True, False)
        player_image_size: V2 = V2.to_v2(player_image_xflipped.get_size())
        IMAGE_SCALE = .15
        return pygame.transform.scale(
            player_image_xflipped,
            (player_image_size.x*IMAGE_SCALE, player_image_size.y*IMAGE_SCALE))

    def hp(self) -> HP:
        return self.__hp

    def render(self) -> None:
        self.__screen.blit(self.__image, self.pos.to_tuple())

    def update(self, dt: float) -> None:
        if not self.__ctrlable:
            return
        key_pressed: pygame.ScancodeWrapper = pygame.key.get_pressed()
        if key_pressed[KEY_SHOT]:
            self.__gun.shot(self.__grade)
        if not key_pressed[KEY_MOVE_UP | KEY_MOVE_LEFT | KEY_MOVE_DOWN | KEY_MOVE_RIGHT]:
            self.__speed.x *= self.__reduction_ratio
            self.__speed.y *= self.__reduction_ratio
            return
        if key_pressed[KEY_MOVE_UP]:
            self.__pos.y -= dt*self.__speed
        if key_pressed[KEY_MOVE_DOWN]:
            self.__pos.y += dt*self.__speed
        if key_pressed[KEY_MOVE_LEFT]:
            self.__pos.x -= dt*self.__speed
        if key_pressed[KEY_MOVE_RIGHT]:
            self.__pos.x += dt*self.__speed

    @property
    def controllable(self) -> bool:
        return self.__ctrlable

    @controllable.setter
    def controllable(self, boo: bool) -> None:
        self.__ctrlable = boo

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
