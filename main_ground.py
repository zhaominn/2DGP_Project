from pico2d import load_image, draw_rectangle


class MainGround:
    def __init__(self):
        self.image = load_image('image//stage1_main//spring_ground_all.png') # 기본 화면

    def draw(self):
        self.image.clip_draw(0, 0, 1600, 800, 1600 / 2, 800 / 2)
        draw_rectangle(*self.get_crop_bb())
        draw_rectangle(*self.get_house_bb())
        draw_rectangle(*self.get_coop_bb())
        draw_rectangle(*self.get_mine_bb())

    def update(self):
        pass

    def get_bb(self):
        return 0,0,1600,800

    def get_crop_bb(self):
        return 1275,330,1325,430

    def get_house_bb(self):
        return 910,480,960,580

    def get_coop_bb(self):
        return 190,370,245,470

    def get_mine_bb(self):
        return 520,660,570,740