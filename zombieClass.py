import AllObjectClass
import gamePlay
import game_framework
from pico2d import *
import marketClass
from path import *
import random
from BehaviorTree import BehaviorTree, SelectorNode, SequenceNode, LeafNode

PIXEL_PER_METER = 10.0 / 0.1
RUN_SPEED_KMPH = 5.0
RUN_SPEED_MPM = RUN_SPEED_KMPH * 1000.0 / 60.6
RUN_SPEED_MPS = RUN_SPEED_MPM / 60.0
RUN_SPEED_PPS = RUN_SPEED_MPS * PIXEL_PER_METER


TIME_PER_ACTION = 2
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 4

TIME_PER_ACTION_BUBBLE = 0.7
ACTION_PER_TIME_BUBBLE = 1.0 / TIME_PER_ACTION_BUBBLE
FRAMES_PER_ACTION_BUBBLE = 4

class Zombie:
    zombieWidth = 160
    zombieHeight = 180
    Genders = [("character1.6\\girl.png",
                "character1.6\\girlB.png"),
               ("character1.6\\boy.png",
                "character1.6\\boyB.png")]
    menu = ['bloodAme', 'Latte']
    orderSignal = 'bubble\\signal.png'
    moveChoice = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    bar = "bubble\\bar.png"
    gauge = "bubble\\gauge.png"

    def __init__(self):
        image, BirthImage = random.choice(Zombie.Genders)
        self.image = load_image(image)
        self.BirthImage = load_image(BirthImage)
        self.bubbleImage = load_image(Zombie.orderSignal)
        self.bar = load_image(Zombie.bar)
        self.gauge = load_image(Zombie.gauge)
        self.BirthingBool = True
        self.bubbleFrame = 0
        self.chairX, self.chairY = 0, 0
        self.frame, self.line = 0, 0
        self.xPos, self.yPos = random.randrange(gamePlay.WIDTH), random.randrange(gamePlay.entranceY)
        self.xDir, self.yDir = 0, 0
        self.timer = 1.0
        self.wait_timer = 2.0
        self.birthingTime = 3
        self.birthCount = 0
        self.dirX, self.dirY = 0, 0
        self.SittingTable = None
        self.menu = None
        self.down = self.yPos - Zombie.zombieHeight / 2
        self.speed = RUN_SPEED_PPS
        self.build_behavior_tree()
        self.waitingTime = 30
        self.readyOrder, self.orderCheck, self.waitngOrder = False, False, False
        self.success, self.fail = False, False

    def update(self):
        self.bt.run()
        if self.readyOrder:
            self.bubbleFrame = (self.bubbleFrame +
                                FRAMES_PER_ACTION_BUBBLE * ACTION_PER_TIME_BUBBLE * game_framework.frame_time) % 4
        if self.BirthingBool:
            self.birthCount = int((1 - self.birthingTime / 3) * 12)
            self.line = self.birthCount // 4
            self.frame = self.birthCount % 4
            print(self.birthCount, self.line, self.frame)
        else:
            self.xPos = clamp(0, self.xPos + self.speed * self.dirX * game_framework.frame_time, gamePlay.WIDTH)
            self.yPos = clamp(0, self.yPos + self.speed * self.dirY * game_framework.frame_time, gamePlay.HEIGHT)
            self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 4
            if self.speed == 0:
                self.line = 0
            else:
                match (self.dirX, self.dirY):
                    case (1, 0):
                        self.line = 3
                    case (-1, 0):
                        self.line = 2
                    case (0, 1):
                        self.line = 1
                    case (0, -1):
                        self.line = 0
        if self.SittingTable is None:
            self.down = self.yPos - Zombie.zombieHeight / 2

    def draw(self):
        if self.BirthingBool:
            self.BirthImage.clip_draw(Zombie.zombieWidth * int(self.frame),
                                      570 - (Zombie.zombieHeight * (self.line + 1)),
                                      Zombie.zombieWidth, Zombie.zombieHeight,
                                      self.xPos - gamePlay.cameraLEFT, self.yPos - gamePlay.cameraBOTTOM)
        else:
            self.image.clip_draw(Zombie.zombieWidth * int(self.frame),
                                 720 - (Zombie.zombieHeight * (self.line + 1)),
                                 Zombie.zombieWidth, Zombie.zombieHeight,
                                 self.xPos - gamePlay.cameraLEFT, self.yPos - gamePlay.cameraBOTTOM)
            if self.readyOrder:
                self.bubbleImage.clip_draw(int(self.bubbleFrame) * 100, 0, 100, 100,
                                           self.xPos - gamePlay.cameraLEFT,
                                           self.yPos + 120 - gamePlay.cameraBOTTOM, 80, 80)
            if self.waitngOrder:
                self.bar.draw(self.xPos - gamePlay.cameraLEFT, self.yPos + 100 - gamePlay.cameraBOTTOM, 90, 21)
                self.gauge.draw_to_origin(self.xPos - 45 + 4 - gamePlay.cameraLEFT,
                                          self.yPos - 7 + 100 - gamePlay.cameraBOTTOM,
                                          self.waitingTime / 30 * 81, 13)

    def Birth(self):
        self.birthingTime -= game_framework.frame_time
        if self.birthingTime <= 0:
            print('birth success')
            self.BirthingBool = False
            whereToGo = random.choice(Zombie.moveChoice)
            self.dirX = whereToGo[0]
            self.dirY = whereToGo[1]
            self.frame = 0
            self.line = 0
            return BehaviorTree.SUCCESS
        return BehaviorTree.RUNNING

    def Wander(self):
        self.speed = RUN_SPEED_PPS
        self.timer -= game_framework.frame_time
        if self.timer <= 0:
            self.timer = 1.0
            whereToGo = random.choice(Zombie.moveChoice)
            self.dirX = whereToGo[0]
            self.dirY = whereToGo[1]
            print('wander success')
            return BehaviorTree.SUCCESS
        return BehaviorTree.RUNNING

        # else:
        #     return BehaviorTree.RUNNING

    def Wait(self):
        self.speed = 0
        self.wait_timer -= game_framework.frame_time
        if self.wait_timer <= 0:
            self.wait_timer = 2.0
            print('wait success')
            return BehaviorTree.SUCCESS
        return BehaviorTree.RUNNING

    def FindEntrance(self):
        distance = (gamePlay.entranceX - self.xPos) ** 2 + (gamePlay.entranceY - self.yPos) ** 2
        if not gamePlay.entranceX - 50 < self.xPos < gamePlay.entranceX + 50:
            if gamePlay.entranceX - 50 < self.xPos:
                self.dirX, self.dirY = -1, 0
            elif self.xPos < gamePlay.entranceX + 170:
                self.dirX, self.dirY = 1, 0
        elif not gamePlay.entranceY - 10 < self.yPos < gamePlay.entranceY + 10:
            if gamePlay.entranceY - 10 < self.yPos:
                self.dirX, self.dirY = 0, -1
            elif self.yPos < gamePlay.entranceY + 10:
                self.dirX, self.dirY = 0, 1

        if distance < (PIXEL_PER_METER) ** 2:
            self.dirX, self.dirY = 0, 0
            print('find_entrance success')
            return BehaviorTree.SUCCESS
        return BehaviorTree.RUNNING

    def TableCheck(self):
        for furniture in gamePlay.furnitureList:
            if isinstance(furniture, marketClass.Table) and not furniture.sit:
                furniture.sit = True
                furniture.sittingZombie = self
                self.SittingTable = furniture
                self.chairX = (gamePlay.mapstartX + gamePlay.boxSizeW * self.SittingTable.xMapIndex +
                               self.SittingTable.weightMapX * gamePlay.boxSizeW / 2)
                self.chairY = gamePlay.HEIGHT - (
                        gamePlay.mapstartY +
                        gamePlay.boxSizeH * self.SittingTable.yMapIndex +
                        gamePlay.boxSizeH * self.SittingTable.weightMapY -
                        self.SittingTable.furnitureHeight / 2)
                print('table check success')
                return BehaviorTree.SUCCESS
        return BehaviorTree.FAIL

    def MoveToTable(self):
        distance = (self.chairX - self.xPos) ** 2 + (self.chairY - self.yPos) ** 2
        if not self.chairY - 20 < self.yPos < self.chairY + 20:
            if self.chairY - 20 < self.yPos:
                self.dirX, self.dirY = 0, -1
            elif self.yPos < self.chairY + 20:
                self.dirX, self.dirY = 0, 1
        elif not self.chairX - 5 < self.xPos < self.chairX + 5:
            if self.chairX - 10 < self.xPos:
                self.dirX, self.dirY = -1, 0
            elif self.xPos < self.chairX + 10:
                self.dirX, self.dirY = 1, 0


        if distance < (PIXEL_PER_METER) ** 2:
            self.xPos = self.chairX + 50
            self.yPos = self.chairY + 40
            self.down = self.chairY - self.SittingTable.furnitureHeight / 2 - 1
            self.speed = 0
            print('Move to table success')
            return BehaviorTree.SUCCESS
        return BehaviorTree.RUNNING

    def ReadyToOrder(self):
        self.readyOrder = True
        if self.orderCheck:
            menuQueue.append(self.menu)
            self.readyOrder = False
            self.waitngOrder = True
            print('ready to order success.. waiting order')
            return BehaviorTree.SUCCESS
        return BehaviorTree.RUNNING

    def WaitForOrder(self):
        self.waitingTime -= game_framework.frame_time
        if self.waitingTime <= 0 or self.fail:
            menuQueue.pop(0)
            self.SittingTable.sittingZombie = None
            self.SittingTable = None
            print('fail')
            return BehaviorTree.FAIL
        elif self.success:
            self.SittingTable.sittingZombie = None
            self.SittingTable = None
            print('success')
            return BehaviorTree.SUCCESS
        return BehaviorTree.RUNNING

    def GoodBye(self):
        distance = (gamePlay.exitPosX - self.xPos) ** 2 + (gamePlay.exitPosY - self.yPos) ** 2
        if not gamePlay.exitPosX - 40 < self.xPos < gamePlay.exitPosX + 40:
            if gamePlay.exitPosX - 40 < self.xPos:
                self.dirX, self.dirY = -1, 0
            elif self.xPos < gamePlay.exitPosX + 40:
                self.dirX, self.dirY = 1, 0
        elif not gamePlay.exitPosY - 40 < self.xPos < gamePlay.exitPosY + 40:
            if gamePlay.exitPosY - 40 < self.yPos:
                self.dirX, self.dirY = 0, -1
            elif self.yPos < gamePlay.exitPosY + 40:
                self.dirX, self.dirY = 0, 1

        if distance < (PIXEL_PER_METER) ** 2:
            self.dirX = gamePlay.exitPosX
            self.dirY = gamePlay.exitPosX
            gamePlay.zombies.remove(self)
            AllObjectClass.remove_object(self)
            del self
            return BehaviorTree.SUCCESS
        return BehaviorTree.RUNNING

    def build_behavior_tree(self):
        BIRTH = LeafNode("Birth", self.Birth)
        WANDER = LeafNode("Wander", self.Wander)
        WAIT = LeafNode('Wait', self.Wait)
        ENTRANCE = LeafNode("find_entrance", self.FindEntrance)
        CHECKTABLE = LeafNode("tableCheck", self.TableCheck)
        GOTABLE = LeafNode("move_to_table", self.MoveToTable)
        READY = LeafNode("ready_to_order", self.ReadyToOrder)
        WAITORDER = LeafNode("wait_for_coffee", self.WaitForOrder)
        GONE = LeafNode("goodbye", self.GoodBye)

        MAIN = SequenceNode('main_quest')
        MAIN.add_children(CHECKTABLE, GOTABLE, READY, WAITORDER)
        BYE = SequenceNode('good_bye')
        BYE.add_children(ENTRANCE, GONE)
        GETCOFFEE = SequenceNode('get_coffee')
        GETCOFFEE.add_children(ENTRANCE, MAIN, BYE)
        NONCHECK = SelectorNode('check-fail')
        NONCHECK.add_children(GETCOFFEE, GONE)
        WANDERWAIT = SelectorNode('find_or_wander')
        WANDERWAIT.add_children(WANDER, WAIT)
        AFTERBIRTH = SelectorNode('after_birth')
        AFTERBIRTH.add_children(NONCHECK, WANDERWAIT)
        ROOT = SequenceNode('root')
        ROOT.add_children(BIRTH, AFTERBIRTH)

        self.bt = BehaviorTree(ROOT)

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
