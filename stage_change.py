from pico2d import *

import game_framework

class Change_stage:
    def __init__(self):
        self.images = [load_image('image//animation//change_stage//stage_change_%d.png' % x) for x in range(10)]
        self.sound=load_wav('sound//change_stage.wav')
        self.sound.set_volume(30)


    def change_stage(self, next_mode):
        for image in self.images:
            image.draw_now(800,400)
            self.sound.play()
            delay(0.1)
        game_framework.change_mode(next_mode)

    def start_stage(self, now_ground):
        for i in range(9,-1,-1):
            now_ground.draw()
            self.images[i].draw_now(800,400)
            self.sound.play()
            delay(0.1)

