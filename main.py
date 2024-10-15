from pico2d import *
import tkinter

root = tkinter.Tk()

monitor_height = root.winfo_screenheight()
monitor_width = root.winfo_screenwidth()

open_canvas(monitor_width,monitor_height)


while 1:
    delay(0.01)

close_canvas()