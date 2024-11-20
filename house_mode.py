from pico2d import *


import game_framework
import game_world
import play_mode
from Player import Player
from tool import Tool
from house_ground import HouseGround

def handle_events():
    #playerX, playerY= player.get_point()
    events = get_events()
    for event in events:
        if event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        elif game_world.collide_bb(player.get_bb(),(0, 700, 1600, 800)) and event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            game_framework.change_mode(play_mode)
        elif event.type in (SDL_KEYDOWN, SDL_KEYUP):
            player.handle_events(event)

def init():
    global world
    global houseGround
    global player
    global tool


    houseGround = HouseGround()
    game_world.add_object(houseGround, 0)
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