from pico2d import load_image


class Tool:
    def __init__(self):
        self.tool_image = load_image('image//ui//tool.png')
        #self.tool_frame_image = load_image('image//ui//tool_frame.png')
        self.tip_image=load_image('image//ui//tip_emoji_v2.png')

    def draw(self):
        self.tool_image.clip_draw(0, 0, 642, 122, 1600/2, 70)
        #self.tool_frame_image.clip_draw(0, 0,102, 102, monitor_width/2-102 + 102*self.tool_num, 70)
        self.tip_image.clip_draw(0, 0, 120, 124, 100, 700,100,100)

    def update(self):
        pass
