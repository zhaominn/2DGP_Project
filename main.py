from pico2d import *

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
        else:
            if event.type in (SDL_KEYDOWN, SDL_KEYUP):
                player.handle_events(event)

def reset_world():
    global running
    global world
    global Ground
    global player
    global crop_obj
    global tool

    running = True
    world = []

    ground = Ground()
    world.append(ground)
    crop_obj = CropObj()
    world.append(crop_obj)
    player = Player(crop_obj)
    world.append(player)
    tool = Tool()
    world.append(tool)

def update_world():
    for o in world:
        o.update()
    pass

def render_world():
    clear_canvas()
    for o in world:
        o.draw()
    update_canvas()

open_canvas(1600,800)
reset_world()

while running:
    handle_events()
    update_world()
    render_world()
    delay(0.05)

close_canvas()