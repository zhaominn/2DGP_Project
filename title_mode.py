from pico2d import load_image, get_events, clear_canvas, update_canvas
from sdl2 import SDL_KEYDOWN, SDLK_ESCAPE, SDLK_RETURN

import game_framework
import play_mode
import stage_change

def init():
    global image
    global change_stage

    image=load_image('image//stage0_start//start_image.png')
    change_stage = stage_change.Change_stage()

def finish():
    global image
    del image

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_RETURN):
            change_stage.change_stage(play_mode)


def draw():
    clear_canvas()
    image.clip_draw(0, 0, 1600, 800, 1600/2, 800/2,1600, 800)
    update_canvas()

def update():
    pass

def pause(): pass
def resume(): pass