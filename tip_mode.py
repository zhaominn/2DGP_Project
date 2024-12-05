from pico2d import get_events, clear_canvas, update_canvas
from sdl2 import SDL_MOUSEBUTTONDOWN, SDL_KEYDOWN, SDLK_ESCAPE

import game_framework
import game_world
from Tip import Tip

name = "tip_mode"

def init():
     global tip
     global prev_mode
     prev_mode=game_framework.get_prev_mode()
     tip = Tip(prev_mode)
     game_world.add_object(tip, 3)

def finish():
     game_world.remove_object(tip)

def update():
    game_world.update()

def draw():
    clear_canvas()
    game_world.render()
    update_canvas()

def pause(): pass
def resume():pass

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        elif event.type == SDL_MOUSEBUTTONDOWN:
            game_framework.pop_mode()


