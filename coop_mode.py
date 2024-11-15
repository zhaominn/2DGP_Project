from pico2d import *

import game_framework
import game_world
import play_mode
from Player import Player
from Coop import Cow, Sheep, Pig
from tool import Tool
from coop_ground import CoopGround


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        elif game_world.collide_bb(player.get_bb(), (0,0,1600,100)) and event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            game_framework.change_mode(play_mode)
        elif event.type in (SDL_KEYDOWN, SDL_KEYUP):
                player.handle_events(event)

def init():
    global world
    global coopGround
    global player
    global cows
    global sheeps
    global pigs
    global tool


    coopGround = CoopGround()
    game_world.add_object(coopGround, 0)
    cows =[Cow() for _ in range(4)]
    game_world.add_objects(cows, 1)
    sheeps = [Sheep() for _ in range(4)]
    game_world.add_objects(sheeps, 1)
    pigs = [Pig() for _ in range(4)]
    game_world.add_objects(pigs, 1)
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