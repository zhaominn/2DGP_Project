from pico2d import *


import game_framework
import game_world
import play_mode
from Player import Player
from tool import Tool
from house_ground import HouseGround
from Crop import CropObj

def handle_events():
    #playerX, playerY= player.get_point()
    events = get_events()
    for event in events:
        if event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        elif game_world.collide_bb(player.get_bb(), (0,0,1600,100)) and event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            game_framework.change_mode(play_mode)
        elif game_world.collide_bb(player.get_bb(), houseGround.get_bed_bb()) and event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            sleep()
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

def sleep():
    for j in range(10):
        for i in range(27):
            if CropObj.water_block_positions[i][j]==1:
                if CropObj.seed_block_positions[i][j] == 1:
                    CropObj.seed_block_positions[i][j] = 2
                elif CropObj.seed_block_positions[i][j] == 2:
                    CropObj.seed_block_positions[i][j] = 3
                elif CropObj.seed_block_positions[i][j] == 3:
                    CropObj.seed_block_positions[i][j] = 4
                elif CropObj.seed_block_positions[i][j] == 4:
                    CropObj.seed_block_positions[i][j] = 5
                elif CropObj.seed_block_positions[i][j] == 5:
                    CropObj.seed_block_positions[i][j] = 6
                elif CropObj.seed_block_positions[i][j] == 6:
                    CropObj.seed_block_positions[i][j] = 7

                CropObj.water_block_positions[i][j] = 0

def pause(): pass
def resume():pass