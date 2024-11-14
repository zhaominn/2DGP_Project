from pico2d import load_image

class CropGround:
    def __init__(self):
        #self.ground_image = load_image('image//stage2.2_crop//greenhouse.png')
        self.ground_image = load_image('image//stage2.2_crop//greenhouse.ver2.png')

    def draw(self):
        self.ground_image.clip_draw(0, 0, 1600, 800, 1600 / 2, 800 / 2)

    def update(self):
        pass