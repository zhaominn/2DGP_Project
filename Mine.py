import random

from pico2d import load_image, draw_rectangle, load_wav

import game_world


class Stone:
    stone_image=None
    crash_stone_sound=None

    def __init__(self):
        if Stone.stone_image==None:
            self.stone_image = load_image('image//stage2.1_mine//stones.png')
        self.x, self.y = random.randint(50, 1550), random.randint(50, 630)
        self.stoneNum = random.randint(0, 9)
        self.attackedNum = 0
        self.mining=False
        if Stone.crash_stone_sound == None:
            self.crash_stone_sound=load_wav('sound//crash_stone.wav')
            self.crash_stone_sound.set_volume(30)

    def draw(self):
        self.stone_image.clip_draw(self.stoneNum * 32 + 16 * int(self.attackedNum), 0, 16, 16,
                                        self.x, self.y, 50, 50)
        #draw_rectangle(*self.get_bb())

    def update(self):
        if self.attackedNum >= 1:
            self.attackedNum+=0.1
        if self.attackedNum >= 2:
            game_world.remove_object(self)
        pass

    def get_bb(self):
        return self.x - 25, self.y - 25, self.x + 25, self.y + 25


    def handle_collision(self, group):
        if group == 'player:stones':
            if self.attackedNum < 1:
                self.attackedNum = 1
                self.crash_stone_sound.play()
