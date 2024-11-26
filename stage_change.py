from pico2d import *

import game_framework

class Change_stage:
    def __init__(self):
        self.images = [load_image('image//change_stage//stage_change_%d.png' % x) for x in range(10 + 1)]

    def change_stage(self, next_mode):
        for image in self.images:
            image.draw_now(800,400)
            delay(0.1)
        game_framework.change_mode(next_mode)

    def start_stage(self, now_ground):
        for i in range(10,-1,-1):
            now_ground.draw()
            self.images[i].draw_now(800,400)
            delay(0.1)

