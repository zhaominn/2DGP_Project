from pico2d import load_image


class Tip:
    def __init__(self, prev_mode):
        if prev_mode=='play_mode':
            self.tip_image = load_image('image//ui//play_mode_tip.png')
        elif prev_mode=='house_mode':
            self.tip_image = load_image('image//ui//house_mode_tip.png')
        elif prev_mode=='mine_mode':
            self.tip_image = load_image('image//ui//mine_mode_tip.png')
        elif prev_mode=='crop_mode':
            self.tip_image = load_image('image//ui//crop_mode_tip.png')
        elif prev_mode=='coop_mode':
            self.tip_image = load_image('image//ui//coop_mode_tip.png')


    def draw(self):
        self.tip_image.clip_draw(0, 0, 1300, 650, 1600 / 2, 800/2)

    def update(self):
        pass
