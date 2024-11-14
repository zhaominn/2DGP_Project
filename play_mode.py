from pico2d import *

import coop_mode
import crop_mode
import game_framework
import game_world
import main_ground
import mine_mode
from Crop import CropObj
from Player import Player
from tool import Tool
from main_ground import MainGround

def handle_events():
    #playerX, playerY= player.get_point()
    events = get_events()
    for event in events:
        if event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        elif game_world.collide_bb(player.get_bb(), mainGround.get_crop_bb()) and event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            game_framework.change_mode(crop_mode)
        elif game_world.collide_bb(player.get_bb(), mainGround.get_mine_bb()) and event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            game_framework.change_mode(mine_mode)
        elif game_world.collide_bb(player.get_bb(), mainGround.get_coop_bb()) and event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            game_framework.change_mode(coop_mode)
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
    player = Player()
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