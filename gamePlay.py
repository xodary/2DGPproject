import gamePlay
import marketClass
from std import *
from pico2d import *
from pinnClass import *
# from zombieClass import *
from objectClass import *
import AllObjectClass
import game_framework

mapping = None
mainMapping = [  # 12 + 16 * 2 = 44 // 9 * 3 + 1 = 28
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0,
     1, 0, 0, 1, 1, 1, 0],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0,
     1, 0, 0, 1, 1, 1, 1],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 1, 1, 1, 0],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 1, 1, 1, 1],
    [0, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 1, 1],
    [1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0,
     0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0,
     0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0,
     0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 1, 1, 1],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0,
     0, 0, 0, 0, 1, 1, 1],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0,
     0, 0, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0,
     0, 0, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0,
     0, 0, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0,
     0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
     1, 2, 2, 2, 1, 1, 1],
]
MainMapPlusX, MainMapPlusY = None, None
MAINMAP = None
WIDTH, HEIGHT = None, None
cameraLEFT, cameraBOTTOM = None, None
viewWIDTH, viewHEIGHT = None, None
boxSizeW = None
boxSizeH = None
mapstartX = None
mapstartY = None
background = None
wallTop = None
wallBottom = None
fence = None
fireobj = None
kitchenTables = None
tables = None
chairs = None
trashes = None
machines = None
bloods = None
milkBoxes = None
cuptablesSmall = None
holding = None
x, y = 0, 0
furnitureList = []
save = [[] for n in range(7)]


def enter():
    global mapping, MainMapPlusX, MainMapPlusY, MAINMAP
    mapping = mainMapping
    MainMapPlusX, MainMapPlusY = 18, 9

    global WIDTH, HEIGHT, cameraLEFT, cameraBOTTOM, viewWIDTH, viewHEIGHT, boxSizeW, boxSizeH, mapstartX, mapstartY
    MAINMAP = True
    WIDTH, HEIGHT = 2560, 1600
    cameraLEFT, cameraBOTTOM = 640, 320
    viewWIDTH, viewHEIGHT = 1920, 1280
    boxSizeW = 56
    boxSizeH = 56
    mapstartX = 54
    mapstartY = 20

    global pinn, background
    background = BackGround('map1.6\\mapBig.png')
    AllObjectClass.add_object(background, 0)
    pinn = Pinn()
    AllObjectClass.add_object(pinn, 1)

    # global zombies
    # zombies = [Zombie()]

    global wallTop, wallBottom, fence, fireobj
    wallTop = WALL(1008, 404, 1001, 120, 'map1.6\\walltop.png')
    AllObjectClass.add_object(wallTop, 1)
    wallBottom = WALL(1008, 964, 1001, 121, 'map1.6\\wall.png')
    AllObjectClass.add_object(wallBottom, 1)
    fence = WALL(0, HEIGHT - 97, 2560, 97, 'map1.6\\fence.png')
    AllObjectClass.add_object(fence, 1)
    fireobj = fire(2364, 1364, 332 // 4, 145, 'map1.6\\fire.png')
    AllObjectClass.add_object(fireobj, 1)

    # global bloodAmericano, Latte
    # bloodAmericano = load_image('order\\bloodAmericano.png')
    # Latte = load_image('order\\Latte.png')

    global kitchenTables, tables, chairs, trashes, machines, bloods, milkBoxes, cuptablesSmall

    milkBoxes = marketClass.Myitem('UI\\milkSell.png', 'UI\\milkBigIcon.png',
                                   'UI\\milkSmallIcon.png', 'map1.6\\milkBox.png',
                                   189, 735, 750, 230, 1, 2, 2, 1, 81, 142, bubbleImage='bubble\\milk.png')
    machines = marketClass.Myitem('UI\\machineSell.png', 'UI\\machineBigIcon.png',
                                  'UI\\machineSmallIcon.png', 'map1.6\\machine.png',
                                  189, 408, 750, 300, 1, 2, 2, 1, 84, 194, bubbleImage="bubble\\coffee.png")
    trashes = marketClass.Myitem('UI\\orderBin.png', 'UI\\binBigIcon.png', 'UI\\binSmallIcon.png', 'map1.6\\trash.png',
                                 189, 270, 749, 147, 1, 1, 1, 1, 56, 94, )
    cuptablesSmall = marketClass.Myitem('UI\\orderShelf.png', 'UI\\shelfBigIcon.png',
                                        'UI\\shelfSmallIcon.png', 'map1.6\\cuptableSmall.png',
                                        189, 450, 749, 211, 2, 2, 2, 1, 99, 174, bubbleImage='bubble\\cup.png')
    tableList = [
        [1, 1, 0],
        [1, 1, 1]
    ]

    # table 가구 이미지 변경(의자랑 합치기)
    tables = marketClass.Myitem('UI\\orderTable.png', 'UI\\tableBigIcon.png',
                                'UI\\tableSmallIcon.png', 'map1.6\\tableandchair.png',
                                189, 700, 749, 197, 3, 2, 4, 2, 216, 147, tableList)
    bloods = marketClass.Myitem('UI\\orderBlood.png', 'UI\\bloodBigIcon.png', 'UI\\bloodSmallIcon.png',
                                'map1.6\\water.png',
                                189, 270, 749, 293, 1, 2, 2, 1, 73, 249, bubbleImage='bubble\\blood.png')
    kitchenTableList = [
        [0, 0, 1],
        [1, 1, 1]
    ]
    kitchenMapList = [
        [0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1],
    ]
    kitchenTables = marketClass.Myitem('UI\\orderKitchenTable.png', 'UI\\kitchenTableBigIcon.png',
                                       'UI\\kitchenTableSmallIcon.png', "map1.6\\kitchenTable.png",
                                       189, 270, 749, 295, 3, 2, 8, 5, 477, 315, kitchenTableList, kitchenMapList)

    Pinn.myitems = [
        [machines, bloods, milkBoxes, cuptablesSmall, cuptablesSmall, trashes],
        [machines, bloods, milkBoxes, cuptablesSmall, cuptablesSmall, None],
        [tables, tables, None, None, None, kitchenTables],
        [tables, tables, tables, kitchenTables, kitchenTables, kitchenTables],
        [None, None, None, None, None, None],
        [None, None, None, None, None, None]
    ]
    machines.yIndex, machines.xIndex, machines.fit = 0, 0, True
    bloods.yIndex, bloods.xIndex, bloods.fit = 0, 1, True
    milkBoxes.yIndex, milkBoxes.xIndex, milkBoxes.fit = 0, 2, True
    cuptablesSmall.yIndex, cuptablesSmall.xIndex, cuptablesSmall.fit = 0, 3, True
    kitchenTables.yIndex, kitchenTables.xIndex, kitchenTables.fit = 2, 3, True
    tables.yIndex, tables.xIndex, tables.fit = 2, 0, True
    trashes.yIndex, trashes.xIndex, trashes.fit = 0, 5, True

    pinnClass.Pinn.myitemList += (milkBoxes, bloods, kitchenTables, cuptablesSmall, machines, tables, trashes)
    AllObjectClass.add_objects(furnitureList, 1)
    gamePlay.pinn.InventoryTest()


def update():
    for object in AllObjectClass.all_objects():
        object.update()
    if holding:
        holding.update()



def handle_events():
    events = get_events()
    global holding, x, y
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type == SDL_MOUSEMOTION or
              event.type == SDL_MOUSEBUTTONDOWN or
              event.type == SDL_MOUSEBUTTONUP):
            x, y = event.x, viewHEIGHT - event.y
            if event.type == SDL_MOUSEBUTTONDOWN:
                holding = pinn.myInventory.MouseButtonDown(x, y)
            elif event.type == SDL_MOUSEMOTION:
                pinn.myInventory.MouseMotion(x, y, holding)
            elif event.type == SDL_MOUSEBUTTONUP:
                pinn.myInventory.MouseButtonUp(holding)
                holding = None
        else:
            pinn.handle_events(event)

def draw():
    clear_canvas()
    for object in AllObjectClass.all_objects():
        object.draw()

    update_canvas()


def exit():
    global pinn
    del pinn


def pause():
    global save
    for n in range(7):
        for objects in AllObjectClass.objects[n]:
            save[n].append(objects)
    AllObjectClass.clear()
    global mainMapping
    mainMapping = mapping


def resume():
    global save
    AllObjectClass.objects = save
    save = [[] for n in range(7)]
    global mapping, MainMapPlusX, MainMapPlusY, MAINMAP
    mapping = mainMapping
    MainMapPlusX, MainMapPlusY = 18, 9

    global WIDTH, HEIGHT, cameraLEFT, cameraBOTTOM, viewWIDTH, viewHEIGHT, boxSizeW, boxSizeH, mapstartX, mapstartY
    MAINMAP = True
    WIDTH, HEIGHT = 2560, 1600
    cameraLEFT, cameraBOTTOM = 640, 0
    viewWIDHT, viewHEIGHT = 1920, 1280
    boxSizeW = 56
    boxSizeH = 56
    mapstartX = 54
    mapstartY = 20

def load_saved_world():
    AllObjectClass.load()
    global pinn
    for o in AllObjectClass.all_objects():
        if isinstance(o, pinnClass.Pinn):
            pinn = o