import os
import pygame

from trrne.v2 import V2
from config import *


class PlayerBullet:
    def __init__(self, screen: pygame.Surface, spawn_pos: V2, speed: float = 20) -> None:
        self.__screen: pygame.Surface = screen
        self.__sprite: pygame.Surface = self.load_sprite()
        self.__DIRECTION: V2 = V2(1, 0)
        self.__speed: float = speed

        self.__pos = spawn_pos

    def load_sprite(self) -> pygame.Surface:
        player_image: pygame.Surface = pygame.image.load(
            os.path.join(PLAYER_PATH_PREFIX, PLAYER_BULLET_NAME))
        player_image_xflipped: pygame.Surface = pygame.transform.flip(
            player_image, True, False)
        player_image_size: V2 = V2.to_v2(player_image_xflipped.get_size())
        IMAGE_SCALE = .15
        return pygame.transform.scale(
            player_image_xflipped,
            (player_image_size.x*IMAGE_SCALE, player_image_size.y*IMAGE_SCALE))

    def render(self) -> None:
        self.__screen.blit(self.__sprite, self.__pos.to_tuple())

    def update(self) -> None:
        self.__pos += self.__DIRECTION*self.__speed
