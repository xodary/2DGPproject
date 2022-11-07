from std import *
from pico2d import *
from pinnClass import *
# from zombieClass import *
from objectClass import *
import AllObjectClass
import game_framework
import gamePlay
import marketClass

cup = None
machine = None
milk = None


def enter():
    Menu = WALL(0, 0, 1920, 1280, 'UI\\marketUI.png')
    AllObjectClass.add_object(Menu, 4)
    global cup, machine, milk
    cup = marketClass.marketSell('UI\\cupSell.png', 'UI\\minicup.png', 189, 270, 750, 121, 1, 1)
    milk = marketClass.marketSell('UI\\milkSell.png', 'UI\\minicup.png', 189, 735, 750, 230, 1, 2)
    machine = marketClass.marketSell('UI\\machineSell.png', 'UI\\minicup.png', 189, 408, 750, 300, 1, 2)
    AllObjectClass.add_object(cup, 5)
    AllObjectClass.add_object(milk, 5)
    AllObjectClass.add_object(machine, 5)

def update():
    # for object in AllObjectClass.all_objects():
    #     object.update()
    pass

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT or event.key == SDLK_ESCAPE:
            game_framework.quit()
        # elif event.type == SDL_KEYDOWN or event.key == SDLK_SPACE:
        #     game_framework.pop_state()
        elif event.type == SDL_MOUSEMOTION:
            x, y = event.x, event.y


def draw():

    clear_canvas()
    for object in AllObjectClass.all_objects():
        object.draw()

    update_canvas()
    delay(0.05)



def exit():
    AllObjectClass.clear()

def pause():
    pass

def resume():
    pass