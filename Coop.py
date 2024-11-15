import random

from pico2d import load_image, get_time, draw_rectangle

import coop_mode
import game_framework

# Animal Run Speed
PIXEL_PER_METER = (10.0 / 1) # 10 pixel 30 cm
RUN_SPEED_KMPH = 20.0 # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# Animal Action Speed
TIME_PER_ACTION = 0.4  # 행동 하나에 걸리는 시간(초)
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION  # 초당 행동 횟수
FRAMES_PER_ACTION = 4


def update_animals_positions(animal):
    animal.frame = 0
    animal.dir = random.randint(0, 1)
    animal.action = random.randint(0, 2)
    animal.start_time = get_time()

class Cow:
    cow_image = None
    block_width = 32
    block_height = 32

    def __init__(self):
        if Cow.cow_image == None:
            self.cow_image = load_image('image//stage2.3_coop//cow.png')
        self.x,self.y=random.randint(100,1500),random.randint(150,700)
        self.cycle_num = random.randint(5,10)
        self.start_time = get_time()
        self.frame=0
        self.dir = random.randint(0,1)
        self.action = random.randint(0,2)

    def draw(self):
        if self.action==0: # 식빵 굽기 자세
            self.cow_image.clip_draw(
                int(self.frame)*self.block_height, 0, self.block_width, self.block_height,
                self.x, self.y, 100, 100
            )
        elif self.action==1: #위아래
            if self.dir==0: #정면
                self.cow_image.clip_draw(
                    int(self.frame) * self.block_height, 4 * self.block_height, self.block_width, self.block_height,
                    self.x, self.y, 100, 100
                )
            elif self.dir==1: #후면
                self.cow_image.clip_draw(
                    int(self.frame) * self.block_height, 2 * self.block_height, self.block_width, self.block_height,
                    self.x, self.y, 100, 100
                )
        elif self.action == 2: #좌우
            if self.dir==0: #오른쪽
                self.cow_image.clip_composite_draw(
                    int(self.frame) * self.block_height, 3 * self.block_height, self.block_width, self.block_height,
                    0, 'h', self.x, self.y, 100, 100
                )
            elif self.dir==1: #왼쪽
                self.cow_image.clip_draw(
                    int(self.frame) * self.block_height, 3 * self.block_height, self.block_width, self.block_height,
                    self.x, self.y, 100, 100
                )
        draw_rectangle(*self.get_bb())

    def update(self):
        if self.action==0 and self.frame>=3:
            pass
        else:
            self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 4
            if self.action==1: # 위아래
                if self.dir==0: #+
                    if self.y>=70:
                        self.y += -1 * RUN_SPEED_PPS * game_framework.frame_time
                    else: self.dir=1
                elif self.dir==1: #-
                    if self.y<=700:
                        self.y += self.dir * RUN_SPEED_PPS * game_framework.frame_time
                    else: self.dir=0
            elif self.action == 2:
                if self.dir==0: #+
                    if self.x>=70:
                        self.x += -1 * RUN_SPEED_PPS * game_framework.frame_time
                    else: self.dir=1
                elif self.dir==1: #-
                    if self.x<=1530:
                        self.x += self.dir * RUN_SPEED_PPS * game_framework.frame_time
                    else: self.dir=0

        if get_time() - self.start_time > self.cycle_num:
            update_animals_positions(self)
        pass

    def get_bb(self):
        return self.x - 40, self.y - 50, self.x + 40, self.y + 30

class Sheep:
    sheep_image = None
    block_width = 32
    block_height = 32

    def __init__(self):
        if Sheep.sheep_image == None:
            self.sheep_image = load_image('image//stage2.3_coop//sheep.png')
        self.x,self.y=random.randint(100,1500),random.randint(150,700)
        self.cycle_num = random.randint(5,10)
        self.start_time = get_time()
        self.frame=0
        self.dir = random.randint(0,1)
        self.action = random.randint(0,2)

    def draw(self):
        if self.action==0: # 식빵 굽기 자세
            self.sheep_image.clip_draw(
                int(self.frame)*self.block_height, 0, self.block_width, self.block_height,
                self.x, self.y, 100, 100
            )
        elif self.action==1: #위아래
            if self.dir==0: #정면
                self.sheep_image.clip_draw(
                    int(self.frame) * self.block_height, 4 * self.block_height, self.block_width, self.block_height,
                    self.x, self.y, 100, 100
                )
            elif self.dir==1: #후면
                self.sheep_image.clip_draw(
                    int(self.frame) * self.block_height, 2 * self.block_height, self.block_width, self.block_height,
                    self.x, self.y, 100, 100
                )
        elif self.action == 2: #좌우
            if self.dir==0: #오른쪽
                self.sheep_image.clip_composite_draw(
                    int(self.frame) * self.block_height, 3 * self.block_height, self.block_width, self.block_height,
                    0, 'h', self.x, self.y, 100, 100
                )
            elif self.dir==1: #왼쪽
                self.sheep_image.clip_draw(
                    int(self.frame) * self.block_height, 3 * self.block_height, self.block_width, self.block_height,
                    self.x, self.y, 100, 100
                )
        draw_rectangle(*self.get_bb())

    def update(self):
        if self.action==0 and self.frame>=3:
            pass
        else:
            self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 4
            if self.action==1: # 위아래
                if self.dir==0: #+
                    if self.y>=70:
                        self.y += -1 * RUN_SPEED_PPS * game_framework.frame_time
                    else: self.dir=1
                elif self.dir==1: #-
                    if self.y<=700:
                        self.y += self.dir * RUN_SPEED_PPS * game_framework.frame_time
                    else: self.dir=0
            elif self.action == 2:
                if self.dir==0: #+
                    if self.x>=70:
                        self.x += -1 * RUN_SPEED_PPS * game_framework.frame_time
                    else: self.dir=1
                elif self.dir==1: #-
                    if self.x<=1530:
                        self.x += self.dir * RUN_SPEED_PPS * game_framework.frame_time
                    else: self.dir=0

        if get_time() - self.start_time > self.cycle_num:
            update_animals_positions(self)
        pass

    def get_bb(self):
        return self.x - 40, self.y - 50, self.x + 40, self.y + 30

class Pig:
    pig_image = None
    block_width = 32
    block_height = 32

    def __init__(self):
        if Pig.pig_image == None:
            self.pig_image = load_image('image//stage2.3_coop//pig.png')
        self.x,self.y=random.randint(100,1500),random.randint(150,700)
        self.cycle_num = random.randint(5,10)
        self.start_time = get_time()
        self.frame=0
        self.dir = random.randint(0,1)
        self.action = random.randint(0,2)

    def draw(self):
        if self.action==0: # 식빵 굽기 자세
            self.pig_image.clip_draw(
                int(self.frame)*self.block_height, 0, self.block_width, self.block_height,
                self.x, self.y, 100, 100
            )
        elif self.action==1: #위아래
            if self.dir==0: #정면
                self.pig_image.clip_draw(
                    int(self.frame) * self.block_height, 4 * self.block_height, self.block_width, self.block_height,
                    self.x, self.y, 100, 100
                )
            elif self.dir==1: #후면
                self.pig_image.clip_draw(
                    int(self.frame) * self.block_height, 2 * self.block_height, self.block_width, self.block_height,
                    self.x, self.y, 100, 100
                )
        elif self.action == 2: #좌우
            if self.dir==0: #오른쪽
                self.pig_image.clip_composite_draw(
                    int(self.frame) * self.block_height, 3 * self.block_height, self.block_width, self.block_height,
                    0, 'h', self.x, self.y, 100, 100
                )
            elif self.dir==1: #왼쪽
                self.pig_image.clip_draw(
                    int(self.frame) * self.block_height, 3 * self.block_height, self.block_width, self.block_height,
                    self.x, self.y, 100, 100
                )
        draw_rectangle(*self.get_bb())

    def update(self):
        if self.action==0 and self.frame>=3:
            pass
        else:
            self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 4
            if self.action==1: # 위아래
                if self.dir==0: #+
                    if self.y>=70:
                        self.y += -1 * RUN_SPEED_PPS * game_framework.frame_time
                    else: self.dir=1
                elif self.dir==1: #-
                    if self.y<=700:
                        self.y += self.dir * RUN_SPEED_PPS * game_framework.frame_time
                    else: self.dir=0
            elif self.action == 2:
                if self.dir==0: #+
                    if self.x>=70:
                        self.x += -1 * RUN_SPEED_PPS * game_framework.frame_time
                    else: self.dir=1
                elif self.dir==1: #-
                    if self.x<=1530:
                        self.x += self.dir * RUN_SPEED_PPS * game_framework.frame_time
                    else: self.dir=0

        if get_time() - self.start_time > self.cycle_num:
            update_animals_positions(self)
        pass

    def get_bb(self):
        return self.x - 40, self.y - 50, self.x + 40, self.y + 30