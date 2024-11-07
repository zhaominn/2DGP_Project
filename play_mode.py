from pico2d import *

import game_framework
import game_world
from Crop import CropObj
from Player import Player
from tool import Tool
from main_ground import MainGround


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        elif event.type in (SDL_KEYDOWN, SDL_KEYUP):
                player.handle_events(event)

def init():
    global world
    global mainGround
    global player
    global crop_obj
    global tool


    mainGround = MainGround()
    game_world.add_object(mainGround, 0)
    crop_obj = CropObj()
    game_world.add_object(crop_obj, 1)
    player = Player(crop_obj)
    game_world.add_object(player, 2)
    tool = Tool()
    game_world.add_object(tool, 2)
    pass

def finish():
    game_world.clear()
    pass

def update():
    game_world.update()

def draw():
    clear_canvas()
    game_world.render()
    update_canvas()

def pause(): pass
def resume():pass