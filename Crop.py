from pico2d import load_image

import game_framework

def water_crop(x, y, cropObj): # 물주기
    if game_framework.get_mode()=='crop_mode':
        cropObj.set_water_position(x, y)

def crop_crop(x, y, cropObj): # 괭이
    if game_framework.get_mode() == 'crop_mode':
        cropObj.set_crop_position(x, y)

def seed_crop(x, y, cropObj): # 괭이
    if game_framework.get_mode() == 'crop_mode':
        cropObj.set_seed_position(x, y)

class CropObj:
    water_image=None
    crop_image=None
    seed_image=None
    block_width=53
    water_block_positions=[[{i*10+j:0} for j in range(10)] for i in range(27)] # 배열 인덱스
    crop_block_positions=[[{i*10+j:0} for j in range(10)] for i in range(27)] # 배열 인덱스
    seed_block_positions=[[{i*10+j:0} for j in range(10)] for i in range(27)] # 배열 인덱스
    def __init__(self):
        if CropObj.water_image == None:
            self.water_image = load_image('image//stage2.2_crop//water.png')
        if CropObj.crop_image == None:
            self.crop_image = load_image('image//stage2.2_crop//crop.png')
        if CropObj.seed_image == None:
            self.seed_image = load_image('image//stage2.2_crop//pumpkin.png')

    def set_water_position(self,x,y):
        for j in range(10):
            for i in range(27):
                # 특정 블록의 좌표 범위 내에 있는지 확인
                if (86 + self.block_width * i <= x < 86 + self.block_width * (i + 1) and
                        83 + self.block_width * j <= y < 83 + self.block_width * (j + 1)):
                    if CropObj.crop_block_positions[i][j] == 1:
                        self.water_block_positions[i][j] = 1
                        return 86 + self.block_width * i, 83 + self.block_width * j

    def set_crop_position(self,x,y):
        for j in range(10):
            for i in range(27):
                # 특정 블록의 좌표 범위 내에 있는지 확인
                if (86 + self.block_width * i <= x < 86 + self.block_width * (i + 1) and
                        83 + self.block_width * j <= y < 83 + self.block_width * (j + 1)):
                    self.crop_block_positions[i][j] = 1
                    return 86 + self.block_width * i, 83 + self.block_width * j

    def set_seed_position(self,x,y):
        for j in range(10):
            for i in range(27):
                # 특정 블록의 좌표 범위 내에 있는지 확인
                if (86 + self.block_width * i <= x < 86 + self.block_width * (i + 1) and
                        83 + self.block_width * j <= y < 83 + self.block_width * (j + 1)):
                    if CropObj.water_block_positions[i][j] == 1:
                        self.seed_block_positions[i][j] = 1
                        return 86 + self.block_width * i, 83 + self.block_width * j

    def draw(self):
        for j in range(10):
            for i in range(27):
                if CropObj.crop_block_positions[i][j] == 1:
                    self.crop_image.clip_draw(0, 0, self.block_width, self.block_width,
                                         86 + self.block_width * i + 26,
                                         83 + self.block_width * j + 26)
                if CropObj.water_block_positions[i][j] == 1:
                    self.water_image.clip_draw(0, 0, self.block_width, self.block_width,
                                         86 + self.block_width * i + 26,
                                         83 + self.block_width * j + 26)
                if CropObj.seed_block_positions[i][j] == 1:
                    self.seed_image.clip_draw(0 * 16, 0, 16, 20,
                                        86 + self.block_width * i + 26,
                                        83 + self.block_width * j + 26, 36, 45)
                elif CropObj.seed_block_positions[i][j] == 2:
                    self.seed_image.clip_draw(1 * 16, 0, 16, 20,
                                        86 + self.block_width * i + 26,
                                        83 + self.block_width * j + 26, 36, 45)
                elif CropObj.seed_block_positions[i][j] == 3:
                    self.seed_image.clip_draw(2 * 16, 0, 16, 20,
                                        86 + self.block_width * i + 26,
                                        83 + self.block_width * j + 26, 36, 45)
                elif CropObj.seed_block_positions[i][j] == 4:
                    self.seed_image.clip_draw(3 * 16, 0, 16, 20,
                                        86 + self.block_width * i + 26,
                                        83 + self.block_width * j + 26, 36, 45)
                elif CropObj.seed_block_positions[i][j] == 5:
                    self.seed_image.clip_draw(4 * 16, 0, 16, 20,
                                        86 + self.block_width * i + 26,
                                        83 + self.block_width * j + 26, 36, 45)
                elif CropObj.seed_block_positions[i][j] == 6:
                    self.seed_image.clip_draw(5 * 16, 0, 16, 20,
                                        86 + self.block_width * i + 26,
                                        83 + self.block_width * j + 26, 36, 45)

    def update(self):
        pass
