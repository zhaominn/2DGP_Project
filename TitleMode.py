from pico2d import load_image, get_events
from pygame.examples.cursors import image
from sdl2 import SDL_QUIT, SDL_KEYDOWN, SDLK_RETURN


class TitleMode:
    def __init__(self):
        global title_image, title_text_image
        title_image = load_image('image//stage0_start//start_image.png')
        title_text_image = load_image('image//stage0_start//start_text.png')

    def finish(self):
        global title_image, title_text_image
        del image

    def handle_events(self):
        events = get_events()
        for event in events:
            if event.type == SDL_QUIT:
                game_framework.quit()
            elif event.type==SDL_KEYDOWN and event.key == SDLK_RETURN:
                game_framework.quit()
