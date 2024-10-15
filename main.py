from pico2d import *
import tkinter

root = tkinter.Tk()

monitor_height = root.winfo_screenheight()
monitor_width = root.winfo_screenwidth()

class Background:
    stage_num=None #0 시작 화면 1 기본 화면
    def __init__(self):
        self.x, self.y = monitor_width/2, monitor_height/2
        self.image = load_image('image//background//spring_ground.png')
        Background.stage_num=1

    def draw(self):
        self.image.clip_draw(0,0,monitor_width,monitor_height,self.x, self.y)

    def update(self):
        pass

def handle_events():
    global running

    events = get_events()
    for event in events:
        if event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        else:
            pass

def reset_world():
    global running
    global world
    global background

    running = True
    world = []

    background = Background()
    world.append(background)

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
    delay(0.01)

close_canvas()