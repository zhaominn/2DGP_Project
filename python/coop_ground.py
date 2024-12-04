from pico2d import load_image

class CoopGround:
    def __init__(self):
        self.ground_image = load_image('image//stage2.3_coop//coop.png')

    def draw(self):
        self.ground_image.clip_draw(0, 0, 1600, 800, 1600 / 2, 800 / 2)

    def update(self):
        pass