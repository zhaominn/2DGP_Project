from pico2d import *

import game_world
from Crop import CropObj
from Player import Player

class Ground:
    def __init__(self):
        #self.ground_image = load_image('image//stage1_main//spring_ground_all.png') # 기본 화면
        self.ground_image = load_image('image//stage2.2_crop//greenhouse.png')

    def draw(self):
        self.ground_image.clip_draw(0, 0, 1600, 800, 1600/2, 800/2,1600, 800)

    def update(self):
        pass

class Tool:
    def __init__(self):
        self.tool_image = load_image('image//ui//tool.png')
        #self.tool_frame_image = load_image('image//ui//tool_frame.png')

    def draw(self):
        self.tool_image.clip_draw(0, 0, 326, 122, 1600/2, 70)
        #self.tool_frame_image.clip_draw(0, 0,102, 102, monitor_width/2-102 + 102*self.tool_num, 70)

    def update(self):
        pass

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        elif event.type in (SDL_KEYDOWN, SDL_KEYUP):
                player.handle_events(event)

def reset_world():
    global running
    global world
    global Ground
    global player
    global crop_obj
    global tool

    running = True

    ground = Ground()
    game_world.add_object(ground,0)
    crop_obj = CropObj()
    game_world.add_object(crop_obj,1)
    player = Player(crop_obj)
    game_world.add_object(player, 2)
    tool = Tool()
    game_world.add_object(tool, 2)

def update_world():
    game_world.update()

def render_world():
    clear_canvas()
    game_world.render()
    update_canvas()

open_canvas(1600,800)
reset_world()
# game loop
while running:
    handle_events()
    update_world()
    render_world()
    delay(0.03)
# finalization code
close_canvas()
