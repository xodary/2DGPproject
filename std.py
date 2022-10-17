import random
import game_framework
from pico2d import *
import queue

WIDTH, HEIGHT = 1200, 822

stage = 0

# x, y
mapstart = [[229, 293], [], [], [], []]

mapping = [[2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
           [2, 'shot', 'shot', 'blood', 'blood', 'milk', 'milk', 'cup1', 'cup1', 'cup2', 'cup2', 1, 1, 0, 0, 0, 0, 2],
           [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 'empty', 'empty', 2],
           [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 2],
           [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 2],
           [2, 0, 0, 'trash', 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 2],
           [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
           [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'empty', 'empty', 2],
           [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 2],
           [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
           [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]]

menuQueue = []
QueueTime = []

zombieSpawn = 100


class Object:
    def __init__(self, name, x=0, y=0, special=False, width=0, height=0, compareY=0):
        self.name = name
        self.x, self.y = x, y
        self.special = special
        self.width, self.height = width, height
        self.compareY = compareY

    def __lt__(self, obj):
        return self.name < obj.name

    def nonSpecial(self):
        self.name.draw(self.x + self.width // 2,
                       HEIGHT - self.y - self.height // 2)

    def pinnZombieDraw(self):
        self.name.draw()

# 수정 요망 (입구 좌표)
stageEntrance = [[562, HEIGHT - 660],
                 [],
                 [],
                 [],
                 []]

tables = [[[False, 0, HEIGHT - 530, 774, HEIGHT - 370, 2, 15], [False, 1, HEIGHT - 700, 789, HEIGHT - 550, 7, 15]],
          [[False, ], [False, ], [False, ]],
          [[False, ], [False, ], [False, ], [False, ]],
          [[False, ], [False, ], [False, ], [False, ], [False, ]],
          [[False, ], [False, ], [False, ], [False, ], [False, ], [False, ]]]

Looking = [[1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0], [-1, -1], [0, -1], [1, -1]]

orderDown = 0
pinn = None
background = None
kitchenTable = None
kitchenTableCoordinate = [[373, 431], [], [], [], []]

wall = None
wallCoordinate = [[230, 253], [], [], [], []]
bubbleBean = None
bubbleBeanCoordinate = [[273, 183], [], [], [], []]
bubbleBlood = None
bubbleBloodCoordinate = [[343, 150], [], [], [], []]
bubblemilk = None
bubblemilkCoordinate = [[410, 180], [], [], [], []]
zombies = [None]
chair = None
table = None
tableCoordinate = [[[688, 536],],
                   [[],],
                   [[],],
                   [[],],
                   [[],]]
chairCoordinate = [[[759, 483],],
                   [[],],
                   [[],],
                   [[],],
                   [[]]]
bubbleframe = 0
firstbubble = False
bloodAmericano = None
Latte = None
trash = None
trashCoordinate = [[335, 443], [], [], [], []]
bubblecup = None
bubblecup1Coordinate = [[475, 170], [], [], [], []]
bubblecup2Coordinate = [[550, 170], [], [], [], []]
cups = []
realCup = None
