import std
from std import *
from pico2d import *
from objectClass import *
from path import *
import random


class Zombie:
    zombieWidth = 105
    zombieHeight = 120
    Genders = [("character\\girlZombieSprite.png",
                "character\\GirlZombiebirthSprite.png"),
               ("character\\boySprite.png",
                "character\\boyBirthSprite.png")]
    menu = ['bloodAme', 'Latte']

    def __init__(self):
        image, BirthImage = random.choice(Zombie.Genders)
        self.image = load_image(image)
        self.BirthImage = load_image(BirthImage)
        self.xPos = random.randint(mapstartX, WIDTH)
        self.yPos = random.randint(0, HEIGHT - (mapstartY + len(std.mapping) * boxSizeH) - 100)
        random.choice(Zombie.menu)
        self.down = self.yPos - Zombie.zombieHeight / 2
        self.event_que = []
        self.cur_state = None
        # self.cur_state.enter()
        self.frame = 0
        self.line = 0
        self.xPos = 0
        self.yPos = 0
        self.xDir = 0
        self.yDir = 0
        self.xindex = 0
        self.yindex = 0
        self.SittingTable = None
        self.menu = None

    def update(self):
        # self.cur_state.do(self)

        if self.xDir > 0:
            self.line = 3
        elif self.xDir < 0:
            self.line = 2
        elif self.yDir > 0:
            self.line = 1
        else:
            self.line = 0

        self.xPos += 6 * self.xDir
        self.yPos += 6 * self.yDir

    def add_event(self, event):
        self.event_que.inset(0, event)

    def draw(self):
        self.cur_state.draw(self)
#
#
#
#
# class BIRTH:
#     def enter(self):
#         self.birthingTime = 0
#     def exit(self):
#         self.line = 0
#         self.frame = 0
#     def do(self):
#         self.birthingTime = self.birthingTime + 1
#         if self.birthingTime >= 60:
#             self.add_event(BIRTHEND)
#     def draw(self):
#         self.frame = (self.birthingTime // 5) % 4
#         self.line = self.birthingTime // 20
#         self.BirthImage.clip_draw(105 * self.frame, 420 - 130 - 130 * self.line, 105, 130, self.xPos, self.yPos + 40)
#
# class WALK:
#     def enter(self):
#         print('Enter walkCafe')
#
#     def exit(self):
#         print('Enter walkCafe')
#
#     def do(self):
#         # 도착했을 경우
#         if self.yPos > EntranceY:
#             self.add_event(ENTRANCE)
#             self.frame = 0
#             return
#
#         if self.xPos < EntranceX:
#             self.xDir = 1
#             self.yDir = 0
#         elif self.xPos > EntranceX:
#             self.xDir = -1
#             self.yDir = 0
#         elif self.yPos < EntranceY:
#             self.xDir = 0
#             self.yDir = 1
#
#     def draw(self):
#         self.image.clip_draw(Zombie.zombieWidth * (self.frame // 4),
#             480 - (Zombie.zombieHeight * self.line + 1),
#             Zombie.zombieWidth,
#             Zombie.zombieHeight,
#             self.xPos, self.yPos + 40)
#         self.frame = (self.frame + 1) % 16
# class CHECK:
#     def do(self):
#         for table in tables:
#             if table.CHECKTABLE():
#                 table.SIT()
#                 self.SittingTable = table
#                 self.add_event(SUCCESS)
#                 break
#         if self.cur_state != SUCCESS:
#             self.cur_state = FAIL
#         event = event_table[self.cur_state]
#     def draw(self):
#         self.image.clip_draw(Zombie.zombieWidth * (self.frame // 4),
#                              480 - (Zombie.zombieHeight * self.line + 1),
#                              Zombie.zombieWidth,
#                              Zombie.zombieHeight,
#                              self.xPos, self.yPos + 40)
#         self.frame = (self.frame + 1) % 16
#
# class IN:
#     dx = [-1, 1, 0, 0]
#     dy = [0, 0, -1, 1]
#
#     def enter(self):
#         self.path = [[0 for col in range(18)] for row in range(11)]
#         self.xindex = (self.xPos - mapstartX) // boxSizeW
#         self.yindex = HEIGHT - (self.yPos - mapstartY) // boxSizeH
#         self.path = bfs(self.xindex, self.yindex, self.table.xIndex, self.table.yIndex, self.path)
#         self.nx = self.ny = 0
#
#     def exit(self):
#         pass
#
#     def do(self):
#         for i in range(4):
#             if self.path[(self.yPos + dx[i]) // boxSizeH][(self.xPos + dy[i]) // boxSizeW] == 1:
#                 self.yPos += dx[i]
#                 self.xPos += dy[i]
#         if (self.table.xIndex == (self.xPos - mapstartX) // boxSizeW) and \
#                 (self.table.yIndex == HEIGHT - (self.yPos - mapstartY) // boxSizeH):
#             self.add_event(ARRIVAL)
#     def draw(self):
#         self.image.clip_draw(Zombie.zombieWidth * (self.frame // 4),
#                              480 - (Zombie.zombieHeight * self.line + 1),
#                              Zombie.zombieWidth,
#                              Zombie.zombieHeight,
#                              self.xPos, self.yPos + 40)
#         self.frame = (self.frame + 1) % 16
#
#
# class OUT:
#     dx = [1, -1, 0, 0]
#     dy = [0, 0, -1, 1]
#
#     def enter(self):
#         self.path = [[0 for col in range(18)] for row in range(11)]
#         self.xindex = (self.xPos - mapstartX) // boxSizeW
#         self.yindex = HEIGHT - (self.yPos - mapstartY) // boxSizeH
#         self.path = bfs(self.table.xIndex, self.table.yIndex, self.xindex, self.yindex, self.path)
#         self.nx = self.ny = 0
#
#     def exit(self):
#         pass
#
#     def do(self):
#         for i in range(4):
#             if self.path[(self.yPos + dx[i]) // boxSizeH][(self.xPos + dy[i]) // boxSizeW] == 1:
#                 self.yPos += dx[i]
#                 self.xPos += dy[i]
#                 break
#         if self.table.xIndex == (self.xPos - mapstartX) // boxSizeW and\
#             self.table.yIndex == HEIGHT - (self.yPos - mapstartY) // boxSizeH):
#             self.add_event(BYE)
#     def draw(self):
#         self.image.clip_draw(Zombie.zombieWidth * (self.frame // 4),
#                              480 - (Zombie.zombieHeight * self.line + 1),
#                              Zombie.zombieWidth,
#                              Zombie.zombieHeight,
#                              self.xPos, self.yPos + 40)
#         self.frame = (self.frame + 1) % 16
#
# class READY:
#     readyOrder = load_image("order\\bubble\\ready.png")
#     @staticmethod
#     def enter(self):
#         print('ENTER ready')
#
#     @staticmethod
#     def exit(self):
#         print('EXIT ready')
#
#     @staticmethod
#     def do(self):
#         pass
#
#     @staticmethod
#     def draw(self):
#         READY.readyOrder.draw(self.xPos, self.yPos + 120)
#         self.image.clip_draw(105 * (self.frame // 8), 480 - 120 - 120 * 0, 105, 120, self.xPos, self.yPos + 40)
#         self.frame = (self.frame + 1) % 16
#
# class WAIT:
#     bar = load_image("order\\bubble\\bar.png")
#     gauge = load_image("order\\bubble\\gauge.png")
#     @staticmethod
#     def enter():
#         print('ENTER wait')
#
#     @staticmethod
#     def exit(self):
#         if self.result == 'success':
#             self.add_event(DRINK)
#         else:
#             self.add_event(NoDRINK)
#         menuQueue.pop(0)
#
#     @staticmethod
#     def do(self):
#         self.waitingTime += 1
#         if self.waitingTime > 54 * 10:
#             self.add_event(NoDRINK)
#             menuQueue.pop(0)
#             tables[self.tableNum][0] = False
#
#
#     @staticmethod
#     def draw(self):
#         WAIT.bar.draw(self.xPos, self.yPos + 120)
#         for width in range(0, 54 - (self.waitingTime // 10) + 1):
#             WAIT.gauge.draw(self.xPos - 60 // 2 + 3 + width, self.yPos + 120, 1, 8)
#         self.image.clip_draw(105 * (self.frame // 8), 480 - 120 - 120 * 0, 105, 120, self.xPos, self.yPos + 40)
#         self.frame = (self.frame + 1) % 16
#
#
#
# class GOOD:
#     heart = load_image("order\\bubble\\heart.png")
#     @staticmethod
#     def enter(self):
#         print('ENTER success')
#         self.bubbleFrame = 0
#     @staticmethod
#     def exit(self):
#         print('EXIT success')
#
#     @staticmethod
#     def do(self):
#         if self.bubbleCount < 5 * 8 - 1:
#             self.bubbleCount += 1
#         else:
#             self.add_state(BYE)
#             self.table.WAKEUP()
#         self.bubbleFrame = self.bubbleCountArray[self.bubbleCount // 8]
#
#     @staticmethod
#     def draw(self):
#         GOOD.heart.clip_draw(self.bubbleFrame * 50, 0, 50, 50, self.xPos, self.yPos + 120)
#         self.image.clip_draw(105 * (self.frame // 8), 480 - 120 - 120 * 0, 105, 120, self.xPos, self.yPos + 40)
#         self.frame = (self.frame + 1) % 16
#
# class BAD:
#     No = load_image("order\\bubble\\No.png")
#     @staticmethod
#     def enter(self):
#         print('ENTER fail')
#         self.bubbleFrame = 0
#
#     @staticmethod
#     def exit(self):
#         print('EXIT fail')
#
#     @staticmethod
#     def do(self):
#         if self.bubbleCount < 5 * 8 - 1:
#             self.bubbleCount += 1
#         else:
#             self.add_state(BYE)
#             self.table.WAKEUP()
#         self.bubbleFrame = self.bubbleCountArray[self.bubbleCount // 8]
#
#     @staticmethod
#     def draw(self):
#         BAD.No.clip_draw(self.bubbleFrame * 50, 0, 50, 50, self.xPos, self.yPos + 120)
#         self.image.clip_draw(105 * (self.frame // 8), 480 - 120 - 120 * 0, 105, 120, self.xPos, self.yPos + 40)
#         self.frame = (self.frame + 1) % 16
#
# class REMOVE:
#     def draw(self):
#         self.image.clip_draw(Zombie.zombieWidth * (self.frame // 4),
#                              480 - (Zombie.zombieHeight * self.line + 1),
#                              Zombie.zombieWidth,
#                              Zombie.zombieHeight,
#                              self.xPos, self.yPos + 40)
#         self.frame = (self.frame + 1) % 16
