import time

from pico2d import delay


def change_mode(mode):
    global stack
    if len(stack) > 0:
        # execute the current mode's finish function
        stack[-1].finish()
        # remove the current mode
        stack.pop()
    stack.append(mode)
    mode.init()


def push_mode(mode):
    global stack
    if len(stack) > 0:
        stack[-1].pause()
    stack.append(mode)
    mode.init()


def pop_mode():
    global stack
    if len(stack) > 0:
        # execute the current mode's finish function
        stack[-1].finish()
        # remove the current mode
        stack.pop()

    # execute resume function of the previous mode
    if len(stack) > 0:
        stack[-1].resume()


def quit():
    global running
    running = False


def run(start_mode):
    global running, stack
    running = True
    stack = [start_mode]
    start_mode.init()

    global frame_time
    frame_time = 0.0
    current_time = time.time()

    # 고정된 시간 스텝 (기본 1/60초, 즉 60 FPS)
    fixed_time_step = 1.0 / 60.0

    while running:
        stack[-1].handle_events()
        stack[-1].update()
        stack[-1].draw()

        frame_time = time.time() - current_time
        frame_rate = 1.0 / frame_time
        current_time += frame_time

        if frame_time > 1.0 / 15.0:
            frame_time = 1.0 / 15.0

        frame_time = fixed_time_step
        delay(fixed_time_step)

    # repeatedly delete the top of the stack
    while len(stack) > 0:
        stack[-1].finish()
        stack.pop()


def get_mode():
    global stack
    if len(stack) > 0:
        current_mode = stack[-1]
        print('----------------')
        print(getattr(current_mode, 'name', current_mode.__class__.__name__))
        return getattr(current_mode, 'name', current_mode.__class__.__name__)  # 현재 모드의 모듈 이름을 반환
    return None

def get_prev_mode():
    global stack
    if len(stack) > 0:
        current_mode = stack[-2]
        print('----------------')
        print(getattr(current_mode, 'name', current_mode.__class__.__name__))
        return getattr(current_mode, 'name', current_mode.__class__.__name__)  # 현재 모드의 모듈 이름을 반환
    return None