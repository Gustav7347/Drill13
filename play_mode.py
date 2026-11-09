from pico2d import *
import game_framework
import game_world
from boy import Boy
from grass import Grass

item_mode_active = False
item_image = None


def handle_events():
    global boy, item_mode_active

    for event in get_events():
        if event.type == SDL_QUIT:
            game_framework.quit()
            return
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            import title_mode
            game_framework.change_mode(title_mode)
            return
        elif event.type == SDL_KEYDOWN and event.key == SDLK_i:
            item_mode_active = not item_mode_active
            return

        if item_mode_active and event.type == SDL_KEYDOWN:
            if event.key == SDLK_0:
                boy.ball_size = 0
                continue
            elif event.key == SDLK_1:
                boy.ball_size = 21
                continue
            elif event.key == SDLK_2:
                boy.ball_size = 41
                continue

        if event.type == SDL_KEYDOWN and event.key == SDLK_p:
            import pause_mode
            game_framework.push_mode(pause_mode)
            return
        else:
            boy.handle_event(event)


def init():
    global boy, item_mode_active, item_image

    game_world.clear()
    item_mode_active = False
    item_image = load_image('item_select.png')
    boy = Boy()
    game_world.add_oject(boy)

    grass = Grass()
    game_world.add_oject(grass, 0)



def update():
    game_world.update()


def render():
    clear_canvas()
    game_world.render()
    if item_mode_active:
        item_image.draw(400, 300)
    update_canvas()

def finish():
    global item_image

    game_world.clear()
    item_image = None
    item_mode_active = False


def pause():
    pass


def resume():
    pass
