from sdl2 import *


def start_event(e):
    return e[0] =='START'

def space_down(e): #e가 space down 인지 판단 return true or false
     return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_SPACE

def time_out(e):
    return e[0]=='TIME_OUT'

def right_down(e):
    return e[0] =='INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_RIGHT

def right_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_RIGHT

def left_down(e):
    return e[0] =='INPUT' and e[1].type == SDL_KEYDOWN and e[1].key==SDLK_LEFT

def left_up(e):
    return e[0] =='INPUT' and e[1].type == SDL_KEYUP and e[1].key==SDLK_LEFT

def up_down(e):
    return e[0] =='INPUT' and e[1].type == SDL_KEYDOWN and e[1].key==SDLK_UP

def up_up(e):
    return e[0] =='INPUT' and e[1].type == SDL_KEYUP and e[1].key==SDLK_UP

def down_down(e):
    return e[0] =='INPUT' and e[1].type == SDL_KEYDOWN and e[1].key==SDLK_DOWN

def down_up(e):
    return e[0] =='INPUT' and e[1].type == SDL_KEYUP and e[1].key==SDLK_DOWN

def one_down(e):
    return e[0] =='INPUT' and e[1].type == SDL_KEYDOWN and e[1].key==SDLK_1

def one_up(e):
    return e[0] =='INPUT' and e[1].type == SDL_KEYUP and e[1].key==SDLK_1

def two_down(e):
    return e[0] =='INPUT' and e[1].type == SDL_KEYDOWN and e[1].key==SDLK_2

def two_up(e):
    return e[0] =='INPUT' and e[1].type == SDL_KEYUP and e[1].key==SDLK_2

def three_down(e):
    return e[0] =='INPUT' and e[1].type == SDL_KEYDOWN and e[1].key==SDLK_3

def three_up(e):
    return e[0] =='INPUT' and e[1].type == SDL_KEYUP and e[1].key==SDLK_3

def four_down(e):
    return e[0] =='INPUT' and e[1].type == SDL_KEYDOWN and e[1].key==SDLK_4

def four_up(e):
    return e[0] =='INPUT' and e[1].type == SDL_KEYUP and e[1].key==SDLK_4

def five_down(e):
    return e[0] =='INPUT' and e[1].type == SDL_KEYDOWN and e[1].key==SDLK_5

def five_up(e):
    return e[0] =='INPUT' and e[1].type == SDL_KEYUP and e[1].key==SDLK_5

class StateMachine:
    def __init__(self, obj):
        self.obj = obj
        self.event_q=[]

    def start(self, state):
        self.cur_state = state
        self.cur_state.enter(self.obj,('START', 0)) # 가상 이벤트 ㅋㅋ
        #print(f'Enter into {state}')

    def update(self):
        self.cur_state.do(self.obj)
        if self.event_q:
            e = self.event_q.pop(0)
            for check_event, next_state in self.transitions[self.cur_state].items():
                if check_event(e):
                    #rint(f'Exit from {self.cur_state}')
                    self.cur_state.exit(self.obj, e)
                    self.cur_state = next_state
                    print(f'Enter into {next_state}')
                    self.cur_state.enter(self.obj, e)
                    return
            # 이 시점으로 왔다는 것은, event 에 따른 전환 못함.
            #print(f'        WARNING: {e} not handled at state {self.cur_state}')

    def draw(self):
        self.cur_state.draw(self.obj)

    def add_event(self, e):
        print(f'    DEBUG: add event {e}')
        self.event_q.append(e)
        pass

    def set_transitions(self, transitions):
        self.transitions = transitions
        pass

    def get_state(self):
        return self.cur_state

