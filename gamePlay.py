import escFramework
from pinnClass import *
import zombieClass
from objectClass import *
import AllObjectClass
import game_framework

mapping = None
mainMapping = [  # 12 + 16 * 2 = 44 // 9 * 3 + 1 = 28
    [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1,
     1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1,
     0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0],
    [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1,
     1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1,
     0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1,
     1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0],
    [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1,
     1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1,
     1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
    [1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1,
     1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0,
     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0,
     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0,
     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0,
     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0,
     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0,
     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0,
     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0,
     0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0,
     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0,
     0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0,
     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0,
     0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1,
     1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
     1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
     2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1],
]
# 24 * 2 , 6
font = 'neodgm.ttf'
mainMapping[4][46 - 1] = 3
mainMapping[4][47 - 1] = 3
mainMapping[4][48 - 1] = 3
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
animalRoom = False
trees = None
chicken = None
cow = None
x, y = 0, 0
furnitureList = []
save = [[] for n in range(7)]
entranceX, entranceY = 1520, 450
zombies = []
exitPosX, exitPosY = 2260, 10
menuQueueTime = []
menuQueue = []

def enter():
    global mapping, MainMapPlusX, MainMapPlusY, MAINMAP
    mapping = mainMapping
    MainMapPlusX, MainMapPlusY = 36, 9

    global WIDTH, HEIGHT, cameraLEFT, cameraBOTTOM, viewWIDTH, viewHEIGHT, boxSizeW, boxSizeH, mapstartX, mapstartY
    MAINMAP = True
    WIDTH, HEIGHT = 2560, 1600
    cameraLEFT, cameraBOTTOM = 640, 320
    viewWIDTH, viewHEIGHT = 1920, 1280
    boxSizeW = 28
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


    global kitchenTables, tables, chairs, trashes, machines, bloods, milkBoxes, cuptablesSmall, trees, cow, chicken


    trees = marketClass.noWait('UI\\orderFingerTree.png', 'UI\\treeBigIcon.png',
                               'UI\\treeSmallIcon.png', 'map1.6\\fingerTree.png',
                               186, 600, 749, 302, 3, 3, 2, 2, 182, 269, 10,
                               bgm='sound\\tree.wav', bubbleImage='bubble\\blood.png')
    milkBoxes = marketClass.noWait('UI\\milkSell.png', 'UI\\milkBigIcon.png',
                                   'UI\\milkSmallIcon.png', 'map1.6\\milkBox.png',
                                   189, 700, 750, 230, 1, 2, 3, 1, 81, 142, 10,
                                   bgm='sound\\milk.wav', bubbleImage='bubble\\milk.png')
    machines = marketClass.waitingForSecond('UI\\machineSell.png', 'UI\\machineBigIcon.png',
                                            'UI\\machineSmallIcon.png', 'map1.6\\machine.png',
                                            189, 300, 750, 300, 1, 2, 3, 1, 84, 194, 10,
                                            bgm='sound\\machine.wav', bubbleImage="bubble\\coffee.png")
    trashes = marketClass.Myitem('UI\\orderBin.png', 'UI\\binBigIcon.png', 'UI\\binSmallIcon.png', 'map1.6\\trash.png',
                                 189, 270, 749, 147, 1, 1, 2, 1, 56, 94, 4, )
    cuptablesSmall = marketClass.noWait('UI\\orderShelf.png', 'UI\\shelfBigIcon.png',
                                        'UI\\shelfSmallIcon.png', 'map1.6\\cuptableSmall.png',
                                        189, 450, 749, 211, 2, 2, 3, 1, 99, 174, 10,
                                        bgm='sound\\cup.wav', bubbleImage='bubble\\cup.png')
    tableList = [
        [1, 1, 0],
        [1, 1, 1]
    ]

    # table 가구 이미지 변경(의자랑 합치기)
    tables = marketClass.Table('UI\\orderTable.png', 'UI\\tableBigIcon.png',
                               'UI\\tableSmallIcon.png', 'map1.6\\tableandchair.png',
                               189, 700, 749, 197, 3, 2, 8, 1, 216, 147, 10,
                               weightList=tableList)
    bloods = marketClass.waitingForSecond('UI\\orderBlood.png', 'UI\\bloodBigIcon.png', 'UI\\bloodSmallIcon.png',
                                          'map1.6\\water.png',
                                          189, 270, 749, 293, 1, 2, 3, 1, 73, 249, 10,
                                          bgm='sound\\water.wav', bubbleImage='bubble\\blood.png')
    kitchenTableList = [
        [0, 0, 1],
        [1, 1, 1]
    ]
    kitchenMapList = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    ]
    kitchenTables = marketClass.Myitem('UI\\orderKitchenTable.png', 'UI\\kitchenTableBigIcon.png',
                                       'UI\\kitchenTableSmallIcon.png', "map1.6\\kitchenTable.png",
                                       189, 270, 749, 295, 3, 2, 18, 5, 477, 315, 20,
                                       weightList=kitchenTableList, weightMapList=kitchenMapList)
    cow = marketClass.Animal('UI\\orderCow.png', 'UI\\cowBigIcon.png',
                             'UI\\cowSmallIcon.png', 'character1.6\\cow.png',
                             189, 270, 749, 182, 3, 2, 0, 0, 256, 256, 15, bgm='sound\\cow.wav')
    chicken = marketClass.Animal('UI\\orderChicken.png', 'UI\\chickenBigIcon.png',
                                 'UI\\chickenSmallIcon.png', 'character1.6\\chicken.png',
                                 189, 500, 749, 137, 2, 2, 0, 0, 128, 128, 10, bgm='sound\\cow.wav')

    Pinn.myitems = [
        [machines, bloods, None, cuptablesSmall, cuptablesSmall, trashes],
        [machines, bloods, None, cuptablesSmall, cuptablesSmall, None],
        [tables, tables, None, None, None, kitchenTables],
        [tables, tables, tables, kitchenTables, kitchenTables, kitchenTables],
        [None, None, None, None, None, None],
        [None, None, None, None, None, None]
    ]

    pinnClass.Pinn.myitemList += (bloods, kitchenTables, cuptablesSmall, machines, tables, trashes)

    machines.yIndex, machines.xIndex, machines.fit = 0, 0, True
    bloods.yIndex, bloods.xIndex, bloods.fit = 0, 1, True
    cuptablesSmall.yIndex, cuptablesSmall.xIndex, cuptablesSmall.fit = 0, 3, True
    kitchenTables.yIndex, kitchenTables.xIndex, kitchenTables.fit = 2, 3, True
    tables.yIndex, tables.xIndex, tables.fit = 2, 0, True
    trashes.yIndex, trashes.xIndex, trashes.fit = 0, 5, True

    AllObjectClass.add_objects(furnitureList, 1)
    gamePlay.pinn.InventoryTest()

    zombies.append(zombieClass.Zombie())
    for zombie in zombies:
        AllObjectClass.add_object(zombie, 1)

zombieSpawn = 4
def update():
    global zombieSpawn
    zombieSpawn -= game_framework.frame_time
    if zombieSpawn <= 0:
        if len(zombies) < 10:
            newZombie = zombieClass.Zombie()
            zombies.append(newZombie)
            AllObjectClass.add_object(newZombie, 1)
        zombieSpawn = 4

    for object in AllObjectClass.all_objects():
        object.update()
    if holding:
        holding.update()

    global menuQueueTime
    Time = []
    for time in menuQueueTime:
        if time > 0:
            time -= game_framework.frame_time
        Time.append(time)
    menuQueueTime = Time




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
        elif event.key == SDLK_ESCAPE:
            game_framework.push_state(escFramework)
        else:
            pinn.handle_events(event)


def draw():
    clear_canvas()
    for object in AllObjectClass.all_objects():
        object.draw()
    for menuImage in menuQueue:
        menu = load_image(menuImage)
        menu.draw_to_origin(30 + 300 * menuQueue.index(menuImage),
                            viewHEIGHT - (1 - menuQueueTime[menuQueue.index(menuImage)]) * 360)
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
    global mapping, MainMapPlusX, MainMapPlusY, MAINMAP, animalRoom
    mapping = mainMapping
    MainMapPlusX, MainMapPlusY = 36, 9
    global WIDTH, HEIGHT, cameraLEFT, cameraBOTTOM, viewWIDTH, viewHEIGHT, boxSizeW, boxSizeH, mapstartX, mapstartY
    MAINMAP = True
    animalRoom = False
    WIDTH, HEIGHT = 2560, 1600
    viewWIDHT, viewHEIGHT = 1920, 1280
    boxSizeW = 28
    boxSizeH = 56
    mapstartX = 54
    mapstartY = 20


def load_saved_world():
    AllObjectClass.load()
    global pinn
    for o in AllObjectClass.all_objects():
        if isinstance(o, pinnClass.Pinn):
            pinn = o
