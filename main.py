from pico2d import *
from Player import Player
import tkinter


root = tkinter.Tk()

monitor_height = root.winfo_screenheight()
monitor_width = root.winfo_screenwidth()

class Ground:
    def __init__(self):
        self.ground_image = load_image('image//stage1_main//spring_ground_all.png')
        #self.tool_frame_image = load_image('image//ui//tool_frame.png')

    def draw(self):
        self.ground_image.clip_draw(0, 0, 1600, 800, monitor_width/2, monitor_height/2,monitor_width, monitor_height)
        #self.tool_frame_image.clip_draw(0, 0,102, 102, monitor_width/2-102 + 102*self.tool_num, 70)

    def update(self):
        pass

class Tool:
    def __init__(self):
        self.tool_num = 0 # 0 물뿌리개 1 곡괭이 2 괭이

        self.tool_image = load_image('image//ui//tool.png')
        #self.tool_frame_image = load_image('image//ui//tool_frame.png')

    def draw(self):
        self.tool_image.clip_draw(0, 0, 326, 122, monitor_width/2, 70)
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
    global tool

    running = True
    world = []

    ground = Ground()
    world.append(ground)
    player = Player()
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

open_canvas(monitor_width,monitor_height)
reset_world()

while running:
    handle_events()
    update_world()
    render_world()
    delay(0.05)

close_canvas()