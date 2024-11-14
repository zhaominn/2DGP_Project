import random

from pico2d import load_image, draw_rectangle

import mine_mode
import game_framework


class Stone:
    stone_image=None

    def __init__(self):
        if Stone.stone_image==None:
            self.stone_image = load_image('image//stage2.1_mine//stones.png')
        self.x, self.y = random.randint(50, 1550), random.randint(50, 630)
        self.stoneNum = random.randint(0, 10)
        self.attackedNum = 0

    def draw(self):
        self.stone_image.clip_draw(self.stoneNum * 32, 0, 16, 16,
                                        self.x, self.y, 50, 50)
        draw_rectangle(*self.get_bb())

    def update(self):
        pass

    def get_bb(self):
        return self.x - 25, self.y - 25, self.x + 25, self.y + 25
