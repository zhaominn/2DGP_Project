from pico2d import *
import game_framework

import coop_mode as start_mode

open_canvas(1600,800)
game_framework.run(start_mode)
close_canvas()