import pygame
from pygame.locals import *

from config import *
from app import app
from trrne.colour import COLOR
from trrne.v2 import V2

from player.player import Player


def main() -> None:
    core = app(GAME_TITLE, WINDOW_SIZE)
    screen: pygame.Surface = core.screen()
    font30: pygame.font = app.font(size=30)

    v = V2(128, 256)
    print(v.to_string())
    print(-v.to_string())

    # load player sprite
    player = Player(screen=screen, max_hp=100, pos=V2(0, 0), speed=256)

    while app.update():
        screen.fill(COLOR.GREY)
        # pressed: pygame.ScancodeWrapper = pygame.key.get_pressed()

        # update --------------------------
        player.render()
        player.update(dt=app.delta_time())

        # _DEBUG --------------------------
        screen.blit(font30.render(
            str(app.delta_time()), True, COLOR.BLACK), (0, 30 * 0))
        screen.blit(font30.render(
            player.pos.to_string(), True, COLOR.BLACK), (0, 30 * 1))
        screen.blit(font30.render(
            str(core.center()), True, COLOR.BLACK), (0, 30 * 2))

        cursor = app.cursor_pos()
        screen.fill((255, 255, 255, 128), pygame.Rect(
            cursor.x-25, cursor.y-25, 50, 50))


if __name__ == '__main__':
    main()
