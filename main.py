from pico2d import *
import tkinter

root = tkinter.Tk()

monitor_height = root.winfo_screenheight()
monitor_width = root.winfo_screenwidth()

class StageManager:
    stage_num=None #0 시작 화면 1 기본 화면
    def __init__(self):
        self.x, self.y = monitor_width/2, monitor_height/2
        self.stage_num = 0
        self.frame=0

        # 이미지 로딩
        self.background0_image = load_image('image//stage0_start//start_image.png')
        self.background0_text_image = load_image('image//stage0_start//start_text.png')

        self.background1_image = load_image('image//stage1_main//spring_ground.png')
        self.farm_image =load_image('image//stage1_main/farm.png')
        self.greenhouse_image = load_image('image//stage1_main//greenhouse.png')
        self.house_image = load_image('image//stage1_main//house.png')

    def draw(self):
        if self.stage_num == 0:
            self.draw_start_screen()
        elif self.stage_num == 1:
            self.draw_main_screen()

    def draw_start_screen(self):
        self.background0_image.clip_draw(0, 0, monitor_width, monitor_height, self.x, self.y)
        self.background0_text_image.clip_draw(0, 0, 600, 100, self.x, 150+self.frame*3)

    def draw_main_screen(self):
        self.background1_image.clip_draw(0, 0, monitor_width, monitor_height, self.x, self.y)
        self.farm_image.clip_draw(0, 0, 281, 279, 300, 550)
        self.greenhouse_image.clip_draw(0, 0, 280, 400, 1300, 600)
        self.house_image.clip_draw(0, 0, 363, 361, 900, 650)

    def update(self):
        if self.stage_num == 0:
            self.frame=(self.frame+1)%5
            delay(0.1)
        else:
            pass

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
        elif event.type == SDL_KEYUP:
            player.status = 0

def reset_world():
    global running
    global world
    global stage_manager
    global player

    running = True
    world = []

    stage_manager = StageManager()
    world.append(stage_manager)
    player=Player()
    world.append(player)

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