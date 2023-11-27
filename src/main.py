import os

import pygame
from pygame.locals import *

from config import *
from app import app
from trrne.colour import COLOR
from trrne.vec2 import V2

from player.player import Player


def main() -> None:
    core = app(GAME_TITLE, WINDOW_SIZE)
    screen: pygame.Surface = core.screen()
    font30: pygame.font = app.font(size=30)

    dt: int = pygame.time.Clock().tick(GAME_FPS) / 1000
    # dt: int = pygame.time.get_ticks() / 1000

    # player
    player_image: pygame.Surface = pygame.image.load(
        os.path.join(PLAYER_PATH_PREFIX, PLAYER_NAME))
    player_image_xflipped: pygame.Surface = pygame.transform.flip(
        player_image, True, False)
    player_image_size: V2 = V2.to_v2(player_image_xflipped.get_size())
    player_image_scale = .15
    player_image_rescaled: pygame.Surface = pygame.transform.scale(
        player_image_xflipped,
        (player_image_size.x * player_image_scale, player_image_size.y * player_image_scale))
    player: Player = Player(
        screen=screen, image=player_image_rescaled, max_hp=100, pos=V2(0, 0), speed=256)

    while app.update():
        screen.fill(COLOR.GREY)
        pressed: pygame.ScancodeWrapper = pygame.key.get_pressed()

        if pressed[K_SPACE]:
            screen.blit(
                font30.render('SPACE IS DOWN!', True, COLOR.GREEN),
                core.center())

        # update --------------------------
        player.render()
        player.update(dt=app.delta_time())

        # _DEBUG --------------------------
        screen.blit(font30.render(
            str(dt), True, COLOR.BLACK), (0, 30 * 0))
        screen.blit(font30.render(
            player.pos.to_string(), True, COLOR.BLACK), (0, 30 * 1))
        screen.blit(font30.render(
            str(core.center()), True, COLOR.BLACK), (0, 30 * 2))

        cursor: tuple[int, int] = pygame.mouse.get_pos()
        screen.fill((255, 255, 255, 128), pygame.Rect(
            cursor[0], cursor[1], 50, 50))


if __name__ == '__main__':
    main()
