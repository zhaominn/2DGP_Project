import random

from pico2d import load_image

class MineGround:
    def __init__(self):
        self.imageNum = random.randint(0,2)
        if self.imageNum==0:
            self.ground_image = load_image('image//stage2.1_mine//mine_1.png')
        elif self.imageNum==1:
            self.ground_image = load_image('image//stage2.1_mine//mine_2.png')
        elif self.imageNum==2:
            self.ground_image = load_image('image//stage2.1_mine//mine_3.png')

    def draw(self):
        self.ground_image.clip_draw(0, 0, 1600, 800, 1600 / 2, 800 / 2)

    def update(self):
        pass