from pico2d import *
from Crop import CropObj

class Sleep:
    def __init__(self):
        self.images = [load_image('image//animation//sleep//sleep_%d.png' % x) for x in range(1, 10 + 1)]

    def sleep(self, house_ground):
        for j in range(10):
            for i in range(27):
                if CropObj.water_block_positions[i][j] == 1:
                    if CropObj.pumpkin_seed_block_positions[i][j] == 1:
                        CropObj.pumpkin_seed_block_positions[i][j] = 2
                    elif CropObj.pumpkin_seed_block_positions[i][j] == 2:
                        CropObj.pumpkin_seed_block_positions[i][j] = 3
                    elif CropObj.pumpkin_seed_block_positions[i][j] == 3:
                        CropObj.pumpkin_seed_block_positions[i][j] = 4
                    elif CropObj.pumpkin_seed_block_positions[i][j] == 4:
                        CropObj.pumpkin_seed_block_positions[i][j] = 5
                    elif CropObj.pumpkin_seed_block_positions[i][j] == 5:
                        CropObj.pumpkin_seed_block_positions[i][j] = 6
                    elif CropObj.pumpkin_seed_block_positions[i][j] == 6:
                        CropObj.pumpkin_seed_block_positions[i][j] = 7

                    if CropObj.peach_seed_block_positions[i][j] == 1:
                        CropObj.peach_seed_block_positions[i][j] = 2
                    elif CropObj.peach_seed_block_positions[i][j] == 2:
                        CropObj.peach_seed_block_positions[i][j] = 3
                    elif CropObj.peach_seed_block_positions[i][j] == 3:
                        CropObj.peach_seed_block_positions[i][j] = 4
                    elif CropObj.peach_seed_block_positions[i][j] == 4:
                        CropObj.peach_seed_block_positions[i][j] = 5
                    elif CropObj.peach_seed_block_positions[i][j] == 5:
                        CropObj.peach_seed_block_positions[i][j] = 6
                    elif CropObj.peach_seed_block_positions[i][j] == 6:
                        CropObj.peach_seed_block_positions[i][j] = 7

                    CropObj.water_block_positions[i][j] = 0

        for image in self.images:
            image.draw_now(800, 400)
            delay(0.1)

        for i in range(9,-1,-1):
            house_ground.draw()
            print(i)
            self.images[i].draw_now(800,400)
            delay(0.1)