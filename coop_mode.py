from pico2d import *

import game_framework
import game_world
import play_mode
import stage_change
from Player import Player, Feed
from Coop import Cow, Sheep, Pig
from tool import Tool
from coop_ground import CoopGround

name = "coop_mode"

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        elif game_world.collide_bb(player.get_bb(), (0,0,1600,100)) and event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            change_stage.change_stage(play_mode)
        elif event.type in (SDL_KEYDOWN, SDL_KEYUP):
                player.handle_events(event)

def init():
    global world
    global coopGround
    global player
    global cows
    global sheeps
    global pigs
    global tool
    global change_stage
    global bgm

    coopGround = CoopGround()
    game_world.add_object(coopGround, 0)
    cows =[Cow() for _ in range(4)]
    game_world.add_objects(cows, 1)
    sheeps = [Sheep() for _ in range(4)]
    game_world.add_objects(sheeps, 1)
    pigs = [Pig() for _ in range(4)]
    game_world.add_objects(pigs, 1)
    player = Player()
    game_world.add_object(player, 2)
    tool = Tool()
    game_world.add_object(tool, 2)

    game_world.add_collision_pair('player:animals', player, None)
    for cow in cows:
        game_world.add_collision_pair('player:animals', None, cow)
    for sheep in sheeps:
        game_world.add_collision_pair('player:animals', None, sheep)
    for pig in pigs:
        game_world.add_collision_pair('player:animals', None, pig)

    change_stage = stage_change.Change_stage()
    change_stage.start_stage(coopGround)

    bgm = load_wav('sound//animal_background.wav')
    bgm.set_volume(10)
    bgm.repeat_play()

def finish():
    game_world.clear()
    pass

def update():
    game_world.update()
    if player.state_machine.get_state() == Feed:
        game_world.handle_collisions()

def draw():
    clear_canvas()
    game_world.render()
    update_canvas()

def pause(): pass
def resume():pass