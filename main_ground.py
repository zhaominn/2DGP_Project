from pico2d import load_image

class MainGround:
    def __init__(self):
        self.image = load_image('image//stage1_main//spring_ground_all.png') # 기본 화면
        #self.ground_image = load_image('image//stage2.2_crop//greenhouse.png')

    def draw(self):
        self.image.clip_draw(0, 0, 1600, 800, 1600 / 2, 800 / 2, 1600, 800)

    def update(self):
        pass