from pico2d import *
import tkinter

root = tkinter.Tk()

monitor_height = root.winfo_screenheight()
monitor_width = root.winfo_screenwidth()

running = True
open_canvas(monitor_width,monitor_height)

def handle_events():
    global running

    events = get_events()
    for event in events:
        if event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        else:
            pass

while running:
    handle_events()
    delay(0.01)

close_canvas()