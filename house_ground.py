from pico2d import load_image, draw_rectangle


class HouseGround:
    def __init__(self):
        self.ground_image = load_image('image//stage2.0_house//homeground.png')

    def draw(self):
        self.ground_image.clip_draw(0, 0, 1600, 800, 1600 / 2, 800 / 2)
        draw_rectangle(*self.get_bed_bb())

    def update(self):
        pass

    def get_bed_bb(self):
        return 1220, 250, 1415, 450