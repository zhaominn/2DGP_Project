from pico2d import *
import tkinter

root = tkinter.Tk()

monitor_height = root.winfo_screenheight()
monitor_width = root.winfo_screenwidth()

class Background:
    stage_num=None #0 시작 화면 1 기본 화면
    def __init__(self):
        self.x, self.y = monitor_width/2, monitor_height/2
        self.stage_num = 0
        self.frame=0

        # 이미지 로딩
        self.background0_image = load_image('image//stage0_start//start_image.png')
        self.background0_text_image = load_image('image//stage0_start//start_text.png')

        self.background1_image = load_image('image//stage1_background//spring_ground.png')
        self.farm_image =load_image('image///stage1_background/farm.png')
        self.greenhouse_image = load_image('image///stage1_background/greenhouse.png')
        self.house_image = load_image('image///stage1_background/house.png')

    def draw(self):
        if self.stage_num == 0:
            self.draw_start_screen()
        elif self.stage_num == 1:
            self.draw_main_screen()

    def draw_start_screen(self):
        self.background0_image.clip_draw(0, 0, monitor_width, monitor_height, self.x, self.y)
        self.background0_text_image.clip_draw(0, 0, 1200, 200, self.x, 200+self.frame*5)

    def draw_main_screen(self):
        self.background1_image.clip_draw(0, 0, monitor_width, monitor_height, self.x, self.y)
        self.farm_image.clip_draw(0, 0, 281, 279, 300, 550)
        self.greenhouse_image.clip_draw(0, 0, 280, 400, 1300, 600)
        self.house_image.clip_draw(0, 0, 363, 361, 900, 650)

    def update(self):
        if self.stage_num == 0:
            self.frame=(self.frame+1)%3
            delay(0.1)
        else:
            pass

def handle_events():
    global running

    events = get_events()
    for event in events:
        if event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        elif event.key == SDLK_RETURN and background.stage_num == 0:
            background.stage_num = 1
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