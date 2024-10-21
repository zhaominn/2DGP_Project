from pico2d import load_image, delay

import tkinter
root = tkinter.Tk()

monitor_height = root.winfo_screenheight()
monitor_width = root.winfo_screenwidth()

class StageManager:
    stage_num=None #0 시작 화면 1 기본 화면
    def __init__(self):
        self.x, self.y = monitor_width/2, monitor_height/2
        self.stage_num = 0
        self.frame=0

        # 이미지 로딩
        self.background0_image = load_image('image//stage0_start//start_image.png')
        self.background0_text_image = load_image('image//stage0_start//start_text.png')

        self.background1_image = load_image('image//stage1_main//spring_ground.png')
        self.farm_image =load_image('image//stage1_main/farm.png')
        self.greenhouse_image = load_image('image//stage1_main//greenhouse.png')
        self.house_image = load_image('image//stage1_main//house.png')

    def draw(self):
        if self.stage_num == 0:
            self.draw_start_screen()
        elif self.stage_num == 1:
            self.draw_main_screen()

    def draw_start_screen(self):
        self.background0_image.clip_draw(0, 0, monitor_width, monitor_height, self.x, self.y)
        self.background0_text_image.clip_draw(0, 0, 600, 100, self.x, 150+self.frame*3)

    def draw_main_screen(self):
        self.background1_image.clip_draw(0, 0, monitor_width, monitor_height, self.x, self.y)
        self.farm_image.clip_draw(0, 0, 281, 279, 300, 550)
        self.greenhouse_image.clip_draw(0, 0, 280, 400, 1300, 600)
        self.house_image.clip_draw(0, 0, 363, 361, 900, 650)

    def update(self):
        if self.stage_num == 0:
            self.frame=(self.frame+1)%5
            delay(0.1)
        else:
            pass
