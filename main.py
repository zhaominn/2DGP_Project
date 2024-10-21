from pico2d import *
from stageManager import StageManager
import tkinter

root = tkinter.Tk()

monitor_height = root.winfo_screenheight()
monitor_width = root.winfo_screenwidth()

class Player:
    def __init__(self):
        self.status = 0 # 0 idle 1 move 2 crop 3 mine 4 water
        self.dir = 3 # 3 앞 2 뒤 1 왼쪽 0 오른쪽
        self.frame = 0
        self.frame_count = 5  # 프레임 전환 간격을 조정하는 변수

        self.x, self.y = monitor_width / 2, monitor_height / 2

        self.basic_image = load_image('image//Player//player_basic.png')
        self.action_image = load_image('image//Player//player_action.png')

    def draw(self):
        if stage_manager.stage_num != 0:
            if self.status == 0 or self.status==1:
                self.basic_image.clip_draw(96 * self.frame, 96 * self.dir, 96, 96, self.x, self.y,200,200)
            elif self.status >= 2 and self.status <= 4:
                pass

    def update(self):
        if stage_manager.stage_num != 0:
            self.frame_count += 1
            if self.frame_count >= 3:
                if self.status == 1:
                    self.frame=(self.frame+1)%2+2
                else:
                    self.frame=(self.frame+1)%2
                self.frame_count = 0  # 카운터 초기화
        if self.status == 1:
            self.move()

    def move_key(self, dir):#방향 및 상태 변경
        self.status = 1
        self.dir = dir
        self.move()

    def move(self): #움직임
        if player.dir == 3:
            self.y-=7
        elif player.dir == 2:
            self.y+=7
        elif player.dir == 1:
            self.x-=7
        elif player.dir == 0:
            self.x+=7

        self.collision_frame()

    def collision_frame(self):
        if self.x-48<=0 or self.x+48 >= monitor_width or self.y-48<=0 or self.y+48 >= monitor_height:
            if player.dir == 3:
                self.y += 7
            elif player.dir == 2:
                self.y -= 7
            elif player.dir == 1:
                self.x += 7
            elif player.dir == 0:
                self.x -= 7

class Ui:
    def __init__(self):
        self.tool_num = 0 # 0 곡괭이 1 괭이 2 물뿌리개

        self.tool_image = load_image('image//ui//tool.png')
        self.tool_bar_image = load_image('image//ui//tool_bar.png')
        self.tool_frame_image = load_image('image//ui//tool_frame.png')

    def draw(self):
        if stage_manager.stage_num != 0:
            self.tool_bar_image.clip_draw(0, 0, 1600, 112, monitor_width/2, 56)
            self.tool_image.clip_draw(0, 0, 295, 102, 300, 51)
            self.tool_frame_image.clip_draw(0, 0,102, 102, 204 + 96*self.tool_num, 51)

    def update(self):
        pass

def handle_events():
    global running

    events = get_events()
    for event in events:
        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                running = False
            elif stage_manager.stage_num == 0:
                if event.key == SDLK_RETURN:
                    stage_manager.stage_num = 1
            elif stage_manager.stage_num != 0:
                if event.key == SDLK_DOWN:
                    player.move_key(3)
                elif event.key == SDLK_UP:
                    player.move_key(2)
                elif event.key == SDLK_LEFT:
                    player.move_key(1)
                elif event.key == SDLK_RIGHT:
                    player.move_key(0)
                elif event.key == SDLK_1:
                    ui.tool_num=0
                elif event.key == SDLK_2:
                    ui.tool_num = 1
                elif event.key == SDLK_3:
                    ui.tool_num = 2
        elif event.type == SDL_KEYUP:
            player.status = 0

def reset_world():
    global running
    global world
    global stage_manager
    global player
    global ui

    running = True
    world = []

    stage_manager = StageManager()
    world.append(stage_manager)
    player = Player()
    world.append(player)
    ui = Ui()
    world.append(ui)

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
    delay(0.1)

close_canvas()