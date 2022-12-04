import AllObjectClass
import gamePlay
import game_framework
from pico2d import *

background = None
cameraLEFT = 0
cameraBOTTOM = 0
def enter():
    global background, cameraLEFT, cameraBOTTOM
    background = load_image('UI\\exit.png')
    cameraLEFT = gamePlay.cameraLEFT
    cameraBOTTOM = gamePlay.cameraBOTTOM

def update():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.key == SDLK_q:
            game_framework.quit()
        if event.key == SDLK_SPACE:
            game_framework.pop_state()


def draw():
    clear_canvas()
    gamePlay.background.draw()
    background.draw(gamePlay.viewWIDTH // 2, gamePlay.viewHEIGHT // 2)
    update_canvas()



def exit():
    pass


def pause():
    pass


def resume():
    gamePlay.cameraBOTTOM = cameraBOTTOM
    gamePlay.cameraLEFT = cameraLEFT
