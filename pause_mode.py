import game_framework
import game_world
from pico2d import *


def init():
    pass


def finish():
    pass


def handle_events():
    for event in get_events():
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_p:
            game_framework.pop_mode()
            return


def update():
    pass


def render():
    clear_canvas()
    game_world.render()
    draw_rectangle(380, 275, 395, 325, 255, 255, 255, filled=True)
    draw_rectangle(405, 275, 420, 325, 255, 255, 255, filled=True)
    update_canvas()
