from std import *
from pico2d import *
from pinnClass import *
# from zombieClass import *
import objectClass
import AllObjectClass
import game_framework
import gamePlay

marketMapping = [
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 0],
    [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
    [0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]

def enter():
    gamePlay.mapping = marketMapping
    gamePlay.MAINMAP = False
    gamePlay.MainMapPlusX, gamePlay.MainMapPlusY = 0, 0
    gamePlay.WIDTH, gamePlay.HEIGHT = 1920, 1280

    gamePlay.cameraLEFT, gamePlay.cameraBOTTOM = 0, 0
    gamePlay.boxSizeW = 56
    gamePlay.boxSizeH = 56
    gamePlay.mapstartX = 35
    gamePlay.mapstartY = 0

    background = objectClass.WALL(0, 0, 1920, 1280, 'map1.6\\market.png')
    AllObjectClass.add_object(background, 0)
    AllObjectClass.add_object(gamePlay.pinn, 1)
    AllObjectClass.add_object(objectClass.WALL(795, 770, 237, 165, 'map1.6\\flooranimal.png'), 0)
    AllObjectClass.add_object(objectClass.interactionTOOL(0, 12, 4, 5, 252, 491, 'map1.6\\christmas.png'), 1)
    AllObjectClass.add_object(objectClass.Store(13, 14, 8, 5, 420, 462, 'map1.6\\animalmarket.png', 1, 'bubble\\signal.png'), 1)
    AllObjectClass.add_object(objectClass.Store(7, 5, 7, 3, 387, 331, 'map1.6\\shop.png', 2, 'bubble\\signal.png'), 1)
    AllObjectClass.add_object(objectClass.Store(23, 6, 6, 2, 318, 339, 'map1.6\\shop2.png', 0, 'bubble\\signal.png'), 1)
    AllObjectClass.add_object(objectClass.interactionTOOL(24, 13, 2, 2, 158, 232, 'map1.6\\tree.png'), 1)
    gamePlay.pinn.InventoryTest()

def update():
    for object in AllObjectClass.all_objects():
        object.update()
    if holding:
        holding.update()

x, y = 0, 0
holding = None
def handle_events():
    events = get_events()
    global x, y, holding
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type == SDL_MOUSEMOTION or
              event.type == SDL_MOUSEBUTTONDOWN or
              event.type == SDL_MOUSEBUTTONUP):
            x, y = event.x, gamePlay.viewHEIGHT - event.y
            if event.type == SDL_MOUSEBUTTONDOWN:
                holding = gamePlay.pinn.myInventory.MouseButtonDown(x, y)
            elif event.type == SDL_MOUSEMOTION:
                gamePlay.pinn.myInventory.MouseMotion(x, y, holding)
            elif event.type == SDL_MOUSEBUTTONUP:
                gamePlay.pinn.myInventory.MouseButtonUp(holding)
                holding = None
        else:
            gamePlay.pinn.handle_events(event)



def draw():

    clear_canvas()
    for object in AllObjectClass.all_objects():
        object.draw()

    update_canvas()



def exit():
    AllObjectClass.clear()
    global marketMapping
    marketMapping = gamePlay.mapping
    gamePlay.cameraBOTTOM = 0

def pause():
    pass

def resume():
    pass

def test_self():
    import sys
    this_module = sys.modules['__main__']
    pico2d.open_canvas(1920, 1280)
    game_framework.run(this_module)
    pico2d.close_canvas()


if __name__ == '__main__':
    test_self()
