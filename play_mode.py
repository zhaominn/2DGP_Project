from pico2d import *

import coop_mode
import crop_mode
import game_framework
import game_world
import house_mode
import mine_mode
import stage_change
import tip_mode
from Player import Player
from tool import Tool
from main_ground import MainGround

name = "play_mode"

def handle_events():
    #playerX, playerY= player.get_point()
    events = get_events()
    for event in events:
        if event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        elif game_world.collide_bb(player.get_bb(), mainGround.get_crop_bb()) and event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            change_stage.change_stage(crop_mode)
        elif game_world.collide_bb(player.get_bb(), mainGround.get_mine_bb()) and event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            change_stage.change_stage(mine_mode)
        elif game_world.collide_bb(player.get_bb(), mainGround.get_coop_bb()) and event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            change_stage.change_stage(coop_mode)
        elif game_world.collide_bb(player.get_bb(), mainGround.get_house_bb()) and event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            change_stage.change_stage(house_mode)
        elif event.type in (SDL_KEYDOWN, SDL_KEYUP):
                player.handle_events(event)
        elif event.type == SDL_MOUSEBUTTONDOWN:
            mx, my = event.x, 800 - 1 - event.y
            if mx>=50 and mx<=150 and my>=650 and my<=750:
                game_framework.push_mode(tip_mode)


def init():
    global world
    global mainGround
    global player
    global tool
    global change_stage
    global bgm

    mainGround = MainGround()
    game_world.add_object(mainGround, 0)
    player = Player()
    game_world.add_object(player, 2)
    tool = Tool()
    game_world.add_object(tool, 2)

    change_stage = stage_change.Change_stage()
    change_stage.start_stage(mainGround)

    bgm=  load_wav('sound//play_background.wav')
    bgm.set_volume(30)
    bgm.repeat_play()

def finish():
    game_world.clear()
    global bgm
    del bgm
    pass

def update():
    game_world.update()

def draw():
    clear_canvas()
    game_world.render()
    update_canvas()

def pause(): pass
def resume():pass