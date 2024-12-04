from pico2d import *


import game_framework
import game_world
import play_mode
import stage_change
import tip_mode
from Player import Player
from Sleep import Sleep
from tool import Tool
from house_ground import HouseGround

name = "house_mode"

def handle_events():
    #playerX, playerY= player.get_point()
    events = get_events()
    for event in events:
        if event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        elif game_world.collide_bb(player.get_bb(), (0,0,1600,100)) and event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            change_stage.change_stage(play_mode)
        elif game_world.collide_bb(player.get_bb(), houseGround.get_bed_bb()) and event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            sleep.sleep(houseGround)
        elif event.type in (SDL_KEYDOWN, SDL_KEYUP):
            player.handle_events(event)
        elif event.type == SDL_MOUSEBUTTONDOWN:
            mx, my = event.x, 800 - 1 - event.y
            if mx>=50 and mx<=150 and my>=650 and my<=750:
                game_framework.push_mode(tip_mode)

def init():
    global world
    global houseGround
    global player
    global tool
    global change_stage
    global sleep
    global bgm

    houseGround = HouseGround()
    game_world.add_object(houseGround, 0)
    player = Player()
    game_world.add_object(player, 2)
    tool = Tool()
    game_world.add_object(tool, 2)

    change_stage = stage_change.Change_stage()
    change_stage.start_stage(houseGround)

    sleep = Sleep()

    bgm=load_wav('sound//house_background.wav')
    bgm.set_volume(10)
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