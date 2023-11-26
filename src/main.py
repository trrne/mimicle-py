import os
# import numpy as np

import pygame
from pygame.locals import *

from config import *
from app import app
from trrne.colour import COLOR
from trrne.res import Resolution, RESNUM
from trrne.vec2 import V2


def main() -> None:
    # core = app('mimicle-py', Resolution(res=RESNUM.HD))
    core = app('mimicle-py', Resolution(res=RESNUM.HD))
    screen: pygame.Surface = core.screen()
    font30: pygame.font = app.font(None, 30, True)
    print('-----------------------------')
    print(core.resolution().width, core.resolution().height)
    print('-----------------------------')

    player_image: pygame.Surface = pygame.image.load(
        os.path.join(PLAYER_PATH_PREFIX, PLAYER_NAME))
    player_image_xflipped: pygame.Surface = pygame.transform.flip(
        player_image, True, False)
    player_image_base_size: tuple[int, int] = player_image_xflipped.get_size()
    # player_image_size = V2(
    #     player_image_base_size[1], player_image_base_size[0])  # (1200, 1600)
    player_image_size = V2.to_v2(player_image_base_size)
    player_image_scale = .15
    # gcd = np.gcd(player_image_size.y,
    #              player_image_size.x % player_image_size.y)
    player_image_rescaled: pygame.Surface = pygame.transform.scale(
        player_image_xflipped,
        (player_image_size.x * player_image_scale, player_image_size.y * player_image_scale))
    player_pos: V2 = V2(0, 0)
    player_speed: float = 1

    while app.update():
        screen.fill(COLOR.GREY)
        pressed: pygame.ScancodeWrapper = pygame.key.get_pressed()

        screen.blit(player_image_rescaled, player_pos.to_tuple())
        # player_image, True, False), player_pos.to_tuple())
        if pressed[K_w]:
            player_pos.y -= player_speed
        elif pressed[K_s]:
            player_pos.y += player_speed
        elif pressed[K_a]:
            player_pos.x -= player_speed
        elif pressed[K_d]:
            player_pos.x += player_speed

        if pressed[K_SPACE]:
            screen.blit(font30.render('SPACE IS DOWN!',
                        True, COLOR.GREEN), core.center())


if __name__ == '__main__':
    main()
