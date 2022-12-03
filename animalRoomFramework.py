from pico2d import *
# from zombieClass import *
import objectClass
import AllObjectClass
import game_framework
import gamePlay

left = 550
top = 1280 - 569
right = 1500
bottom = 1280 - 550 - 383
width = right - left
height = top - bottom
animalMap = [[0 for n in range(16)] for m in range(7)]
animalMap[0][15] = 1
animalMap[1][15] = 1
animalMap[0][14] = 1
animalMap[1][14] = 1
animalMap[2][15] = 3
animalMap[3][15] = 3
animalMap[4][15] = 3
animalMap[5][15] = 1
animalMap[6][15] = 1
animalMap[5][14] = 1
animalMap[6][14] = 1
animalList = []

def enter():
    gamePlay.mapping = animalMap
    gamePlay.MAINMAP = False
    gamePlay.animalRoom = True
    gamePlay.MainMapPlusX, gamePlay.MainMapPlusY = 0, 0
    gamePlay.WIDTH, gamePlay.HEIGHT = 1920, 1280

    gamePlay.cameraLEFT, gamePlay.cameraBOTTOM = 0, 0
    gamePlay.boxSizeW = width // 16
    gamePlay.boxSizeH = height // 7

    background = objectClass.WALL(0, 0, 1920, 1280, 'map1.6\\animalRoom.png')
    AllObjectClass.add_object(background, 0)

    gamePlay.pinn.x = right - 100
    gamePlay.pinn.y = (bottom + top) / 2
    AllObjectClass.add_object(gamePlay.pinn, 1)
    AllObjectClass.add_objects(animalList, 1)
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
            x, y = event.x, gamePlay.HEIGHT - event.y
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
    gamePlay.cameraBOTTOM = 1600 - 1280

def pause():
    pass

def resume():
    pass
