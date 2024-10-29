from pico2d import load_image
import tkinter
from StateMachine import StateMachine, space_down, right_down, left_down, left_up, right_up, start_event, up_down, \
    down_up, down_down, up_up, two_down, three_down, one_down, one_up, two_up, three_up

root = tkinter.Tk()
monitor_height = root.winfo_screenheight()
monitor_width = root.winfo_screenwidth()

class Idle:
    @staticmethod
    def enter(player,e):
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
        pass

    @staticmethod
    def exit(player,e):
        pass

    @staticmethod
    def do(player):
        player.frame = (player.frame + 1) % 2

    @staticmethod
    def draw(player):
        player.basic_image.clip_draw(player.frame * 96, player.action * 96, 96, 96, player.x, player.y,200,200)

class Run:
    @staticmethod
    def enter(player,e):
        if right_down(e) or right_up(e):
            player.dir, player.action = 1, 0
        elif left_down(e) or left_up(e):
            player.dir, player.action = -1, 1
        elif up_down(e) or down_up(e):
            player.dir, player.action = 1, 2
        elif down_down(e) or up_up(e):
            player.dir, player.action = -1, 3

    @staticmethod
    def exit(player,e):
        pass

    @staticmethod
    def do(player):
        if player.action == 0 or player.action == 1:
            player.x += player.dir * 10
        elif player.action == 2 or player.action == 3:
            player.y += player.dir * 10
        player.frame =(player.frame+1) % 4

    @staticmethod
    def draw(player):
        player.basic_image.clip_draw(
            player.frame * 96, player.action * 96, 96, 96,
            player.x, player.y, 200, 200
        )

class Water:
    @staticmethod
    def enter(player, e):
        pass

    @staticmethod
    def exit(player, e):
        pass

    @staticmethod
    def do(player):
        pass

    @staticmethod
    def draw(player):
       pass

class Mine:
    @staticmethod
    def enter(player, e):
        pass

    @staticmethod
    def exit(player, e):
        pass

    @staticmethod
    def do(player):
        pass

    @staticmethod
    def draw(player):
        pass

class Crop:
    @staticmethod
    def enter(player, e):
        pass

    @staticmethod
    def exit(player, e):
        pass

    @staticmethod
    def do(player):
        pass

    @staticmethod
    def draw(player):
        pass

class Player:
    def __init__(self):
        # 0 idle 1 move 2 water 3 mine 4 crop
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
                       one_down: Water, one_up: Water, two_down: Mine, two_up: Mine, three_down: Crop, three_up: Crop},
                Run: {right_down: Idle, left_down: Idle, right_up: Idle, left_up: Idle,
                      up_down: Idle, down_down: Idle, up_up: Idle, down_up: Idle,
                      one_down: Water, one_up: Water, two_down: Mine, two_up: Mine, three_down: Crop, three_up: Crop},
            }
        )

    #def draw(self):
    #    if self.status == 0 or self.status==1:
    #        self.basic_image.clip_draw(96 * self.frame, 96 * self.dir, 96, 96, self.x, self.y,200,200)
    #    elif self.status >= 2 and self.status <= 4:
    #        self.action_image.clip_draw(96 * self.frame, 384 * (self.status-2) + 96 * self.dir, 96, 96, self.x, self.y, 200, 200)

    def update(self):
        self.state_machine.update()

    def handle_events(self,events):
        # 우리가 state machine 에 전달해 줄 건 튜플 형식 ( , )
        self.state_machine.add_event(
            ('INPUT', events)
        )

    def draw(self):
        self.state_machine.draw()