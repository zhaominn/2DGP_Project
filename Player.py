from pico2d import load_image, get_time, draw_rectangle
import tkinter

from StateMachine import *
from Crop import water_crop, crop_crop, seed_crop
import game_framework

root = tkinter.Tk()
monitor_height = root.winfo_screenheight()
monitor_width = root.winfo_screenwidth()

# Player Run Speed
PIXEL_PER_METER = (10.0 / 0.3) # 10 pixel 30 cm
RUN_SPEED_KMPH = 20.0 # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# Player Action Speed
TIME_PER_ACTION = 0.4  # 행동 하나에 걸리는 시간(초)
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION  # 초당 행동 횟수

class Idle:
    @staticmethod
    def enter(player,e):
        if player.action == 4 or player.action == 8:
            player.dir, player.action = 0, 0
        elif player.action == 5 or player.action == 9:
            player.dir, player.action = 0, 1
        elif player.action == 6 or player.action == 10:
            player.dir, player.action = 0, 2
        elif player.action == 7 or player.action == 11:
            player.dir, player.action = 0, 3

        if left_up(e) or right_down(e):
            player.action = 1
            player.face_dir = -1
        elif right_up(e) or left_down(e):
            player.action = 0
            player.face_dir = 1
        elif start_event(e):
            player.action = 3

        player.dir = 0 # 정지 상태
        player.frame = 0
        player.frame_time = get_time()
        pass

    @staticmethod
    def exit(player,e):
        pass

    @staticmethod
    def do(player):
        player.frame =(player.frame +2* ACTION_PER_TIME * game_framework.frame_time) % 2

    @staticmethod
    def draw(player):
        player.basic_image.clip_draw(int(player.frame) * 96, player.action * 96, 96, 96, player.x, player.y,200,200)

class Run:
    @staticmethod
    def enter(player,e):
        if right_down(e):
            player.dir, player.action = 1, 0
        elif left_down(e):
            player.dir, player.action = -1, 1
        elif up_down(e):
            player.dir, player.action = 1, 2
        elif down_down(e):
            player.dir, player.action = -1, 3

    @staticmethod
    def exit(player,e):
        pass

    @staticmethod
    def do(player):
        if player.action == 0 or player.action == 1:
            player.x += player.dir * RUN_SPEED_PPS * game_framework.frame_time
        elif player.action == 2 or player.action == 3:
            player.y+= player.dir * RUN_SPEED_PPS * game_framework.frame_time
        player.frame =(player.frame+4 * ACTION_PER_TIME * game_framework.frame_time) % 4

    @staticmethod
    def draw(player):
        player.basic_image.clip_draw(
            int(player.frame) * 96, player.action * 96, 96, 96,
            player.x, player.y, 200, 200
        )

class Water:
    @staticmethod
    def enter(player, e):
        if player.action==4 or player.action==8:
            player.action = 0
        elif player.action==5 or player.action==9:
            player.action = 1
        elif player.action==6 or player.action==10:
            player.action = 2
        elif player.action==7 or player.action==11:
            player.action = 3

        water_crop(player.x,player.y, player.cropObj)
        player.start_time = get_time()

    @staticmethod
    def exit(player, e):
        pass

    @staticmethod
    def do(player):
        player.frame =(player.frame+2 * ACTION_PER_TIME * game_framework.frame_time) % 2
        if get_time() - player.start_time > 1:
            player.state_machine.add_event(('TIME_OUT', 0))

    @staticmethod
    def draw(player):
        player.action_image.clip_draw(
            int(player.frame) * 96, player.action * 96, 96, 96,
            player.x, player.y, 200, 200
        )

class Crop:
    @staticmethod
    def enter(player, e):
        if player.action==0 or player.action==4:
            player.action = 8
        elif player.action==1 or player.action==5:
            player.action = 9
        elif player.action==2 or player.action==6:
            player.action = 10
        elif player.action==3 or player.action==7:
            player.action = 11

        crop_crop(player.x, player.y, player.cropObj)
        player.start_time = get_time()

    @staticmethod
    def exit(player, e):
        pass

    @staticmethod
    def do(player):
        player.frame =(player.frame+2 * ACTION_PER_TIME * game_framework.frame_time) % 2
        if get_time() - player.start_time > 1:
            player.state_machine.add_event(('TIME_OUT', 0))

    @staticmethod
    def draw(player):
        player.action_image.clip_draw(
            int(player.frame) * 96, player.action * 96, 96, 96,
            player.x, player.y, 200, 200
        )

class Seed:
    @staticmethod
    def enter(player, e):
        if player.action == 4 or player.action == 8:
            player.dir, player.action = 0, 0
        elif player.action == 5 or player.action == 9:
            player.dir, player.action = 0, 1
        elif player.action == 6 or player.action == 10:
            player.dir, player.action = 0, 2
        elif player.action == 7 or player.action == 11:
            player.dir, player.action = 0, 3


        seed_crop(player.x,player.y, player.cropObj)
        player.dir = 0  # 정지 상태
        player.frame = 0
        player.frame_time = get_time()

    @staticmethod
    def exit(player, e):
        pass

    @staticmethod
    def do(player):
        player.frame = (player.frame + 2 * ACTION_PER_TIME * game_framework.frame_time) % 2

    @staticmethod
    def draw(player):
        player.basic_image.clip_draw(int(player.frame) * 96, player.action * 96, 96, 96, player.x, player.y, 200, 200)

class Mine:
    @staticmethod
    def enter(player, e):
        if player.action==0 or player.action==8:
            player.dir, player.action = 0, 4
        elif player.action==1 or player.action==9:
            player.dir, player.action = 0, 5
        elif player.action==2 or player.action==10:
            player.dir, player.action = 0, 6
        elif player.action==3 or player.action==11:
            player.dir, player.action = 0, 7
        player.start_time = get_time()


    @staticmethod
    def exit(player, e):
        pass

    @staticmethod
    def do(player):
        player.frame =(player.frame+2 * ACTION_PER_TIME * game_framework.frame_time) % 2
        if get_time() - player.start_time > 1:
            player.state_machine.add_event(('TIME_OUT', 0))

    @staticmethod
    def draw(player):
        player.action_image.clip_draw(
            int(player.frame) * 96, player.action * 96, 96, 96,
            player.x, player.y, 200, 200
        )

class Feed:
    @staticmethod
    def enter(player, e):
        if player.action == 4 or player.action == 8:
            player.dir, player.action = 0, 0
        elif player.action == 5 or player.action == 9:
            player.dir, player.action = 0, 1
        elif player.action == 6 or player.action == 10:
            player.dir, player.action = 0, 2
        elif player.action == 7 or player.action == 11:
            player.dir, player.action = 0, 3

        player.dir = 0  # 정지 상태
        player.frame = 0
        player.start_time = get_time()

    @staticmethod
    def exit(player, e):
        pass

    @staticmethod
    def do(player):
        player.frame = (player.frame + 2 * ACTION_PER_TIME * game_framework.frame_time) % 2
        if get_time() - player.start_time > 1:
            player.state_machine.add_event(('TIME_OUT', 0))

    @staticmethod
    def draw(player):
        player.basic_image.clip_draw(int(player.frame) * 96, player.action * 96, 96, 96, player.x, player.y, 200, 200)

class Player:
    def __init__(self,cropObj=None):
        self.cropObj =cropObj
        self.x, self.y = monitor_width / 2, monitor_height / 2
        self.frame = 0
        self.dir = 0
        self.action = 3
        self.basic_image = load_image('image//Player//player_basic.png')
        self.action_image = load_image('image//Player//player_action.png')
        self.state_machine = StateMachine(self)  # 소년 객체의 state machine 생성
        self.state_machine.start(Idle)  # 초기 상태가 idle 로 설정
        self.state_machine.set_transitions(
            {  # dict 를 통해 표현
                Idle: {right_down: Run, left_down: Run, left_up: Run, right_up: Run,
                       up_down: Run, down_down: Run, up_up: Run, down_up: Run,
                       one_down: Mine, one_up: Mine, two_down: Crop, two_up: Crop,
                       three_down: Water, three_up: Water,four_down:Seed,four_up:Seed,
                       five_down:Feed,five_up:Feed},
                Run: {right_down: Idle, left_down: Idle, right_up: Idle, left_up: Idle,
                      up_down: Idle, down_down: Idle, up_up: Idle, down_up: Idle,
                      one_down: Mine, one_up: Mine, two_down: Crop, two_up: Crop,
                      three_down: Water, three_up: Water,four_down:Seed,four_up:Seed,
                       five_down:Feed,five_up:Feed},
                Mine:{right_down: Run, left_down: Run,up_down: Run, down_down: Run,
                       left_up: Run, right_up: Run,up_up: Run, down_up: Run,
                        two_down: Crop, two_up: Crop, three_down: Water,three_up: Water,
                        four_down:Seed,four_up:Seed, five_down:Feed,five_up:Feed,
                      time_out : Idle,},
                Crop:{right_down: Run, left_down: Run,up_down: Run, down_down: Run,
                      left_up: Run, right_up: Run, up_up: Run, down_up: Run,
                        one_down: Mine, one_up: Mine, three_down: Water, three_up: Water,
                      four_down:Seed,four_up:Seed, five_down:Feed,five_up:Feed,
                      time_out : Idle},
                Water: {right_down: Run, left_down: Run,up_down: Run, down_down: Run,
                       left_up: Run, right_up: Run,up_up: Run, down_up: Run,
                        one_down: Mine, one_up: Mine, two_down: Crop, two_up: Crop,
                       four_down:Seed,four_up:Seed, five_down:Feed,five_up:Feed,
                        time_out : Idle},
                Seed: {right_down: Run, left_down: Run,up_down: Run, down_down: Run,
                       left_up: Run, right_up: Run,up_up: Run, down_up: Run,
                        one_down: Mine, one_up: Mine, two_down: Crop, two_up: Crop,
                        three_down: Water, three_up: Water, five_down:Feed,five_up:Feed,
                       time_out : Idle},
                Feed:{right_down: Run, left_down: Run,up_down: Run, down_down: Run,
                       left_up: Run, right_up: Run,up_up: Run, down_up: Run,
                        one_down: Mine, one_up: Mine, two_down: Crop, two_up: Crop,
                        three_down: Water, three_up: Water, four_down:Seed,four_up:Seed,
                       time_out : Idle},
            }
        )

    def update(self):
        self.state_machine.update()

    def handle_events(self,events):
        # 우리가 state machine 에 전달해 줄 건 튜플 형식 ( , )
        self.state_machine.add_event(
            ('INPUT', events)
        )

    def draw(self):
        self.state_machine.draw()
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 30, self.y - 30, self.x + 30, self.y + 30

    def handle_collision(self, group):
        pass