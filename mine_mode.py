import random

from pico2d import *

import game_framework
import game_world
import play_mode
import stage_change
from Mine import Stone
from Player import Player, Mine
from mine_ground import MineGround
from tool import Tool

name = "mine_mode"

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        elif game_world.collide_bb(player.get_bb(), (0,700,1600,800)) and event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            change_stage.change_stage(play_mode)
        elif event.type in (SDL_KEYDOWN, SDL_KEYUP):
                player.handle_events(event)

def init():
    global world
    global mineGround
    global player
    global stones
    global tool
    global change_stage
    global bgm

    mineGround = MineGround()
    game_world.add_object(mineGround, 0)
    stoneNum=random.randint(50,70)
    stones = [Stone() for _ in range(stoneNum)]
    game_world.add_objects(stones, 1)
    player = Player()
    game_world.add_object(player, 2)
    tool = Tool()
    game_world.add_object(tool, 2)

    game_world.add_collision_pair('player:stones', player, None)
    for stone in stones:
        game_world.add_collision_pair('player:stones', None, stone)

    change_stage = stage_change.Change_stage()
    change_stage.start_stage(mineGround)

    bgm=load_wav('sound//mine_background.wav')
    bgm.set_volume(30)
    bgm.repeat_play()

def finish():
    game_world.clear()
    global bgm
    del bgm
    pass

def update():
    game_world.update()
    if player.state_machine.get_state() == Mine:
        game_world.handle_collisions()

def draw():
    clear_canvas()
    game_world.render()
    update_canvas()

def pause(): pass
def resume():pass