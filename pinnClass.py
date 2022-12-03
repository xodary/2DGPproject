import random

import game_framework
from pico2d import *
import zombieClass
import cupClass
import objectClass
import AllObjectClass
import gamePlay
import marketMap
import marketClass

running = True
Looking = [[1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0], [-1, -1], [0, -1], [1, -1]]

RD, LD, RU, LU, ND, SD, NU, SU, STOP, SPACE, ESC, INVEN = range(12)
event_name = ['RD', 'LD', 'RU', 'LU', 'ND', 'SD', 'NU', 'SU', 'STOP', 'SPACE', 'ESC', 'INVEN']

key_event_table = {
    (SDL_KEYDOWN, SDLK_SPACE): SPACE,
    (SDL_KEYDOWN, SDLK_RIGHT): RD,
    (SDL_KEYDOWN, SDLK_LEFT): LD,
    (SDL_KEYUP, SDLK_RIGHT): RU,
    (SDL_KEYUP, SDLK_LEFT): LU,
    (SDL_KEYDOWN, SDLK_UP): ND,
    (SDL_KEYDOWN, SDLK_DOWN): SD,
    (SDL_KEYUP, SDLK_UP): NU,
    (SDL_KEYUP, SDLK_DOWN): SU,
    (SDL_KEYDOWN, SDLK_ESCAPE): ESC,
    (SDL_KEYDOWN, SDLK_e): INVEN,
}



class IDLE:
    def enter(self, event):
        print('Enter IDLE')
        self.line = 0
        if event == INVEN:
            if self.inven != None:
                AllObjectClass.remove_object(self.inven)
                for item in Pinn.myitemList:
                    AllObjectClass.remove_object(item)
                self.inven = None
            else:
                self.inven = self.myInventory
                AllObjectClass.add_object(self.inven, 6)
                for item in Pinn.myitemList:
                    item.add_event(marketClass.MAKESMALLICON)
                    AllObjectClass.add_object(item, 6)
    def exit(self):
        pass
    def do(self):
        self.bubbleCheck()
    def draw(self):

        self.character.clip_draw(self.faceDir * Pinn.pinnImageX,
                                 (2016 - Pinn.pinnImageY * (self.line + 1)),
                                 Pinn.pinnImageX, Pinn.pinnImageY,
                                 self.x - gamePlay.cameraLEFT,
                                 self.y + Pinn.pinnImageY / 2 - 45 - gamePlay.cameraBOTTOM)

class RUN:
    def enter(self, event):

        if event == RD:
            self.dirX += 1
            print('Enter RD')
        elif event == RU:
            self.dirX -= 1
            print('Enter RU')
        elif event == LD:
            self.dirX -= 1
            print('Enter LD')
        elif event == LU:
            self.dirX += 1
            print('Enter LU')
        elif event == ND:
            self.dirY += 1
            print('Enter ND')
        elif event == NU:
            self.dirY -= 1
            print('Enter NU')
        elif event == SD:
            self.dirY -= 1
            print('Enter SD')
        elif event == SU:
            self.dirY += 1
            print('Enter SU')
        elif event == INVEN:
            if self.inven != None:
                AllObjectClass.remove_object(self.inven)
                for item in Pinn.myitemList:
                    AllObjectClass.remove_object(item)
                self.inven = None
            else:
                self.inven = self.myInventory
                AllObjectClass.add_object(self.inven, 6)
                for item in Pinn.myitemList:
                    item.add_event(marketClass.MAKESMALLICON)
                    AllObjectClass.add_object(item, 6)
        self.frame = 0

        match (self.dirX, self.dirY):
            case (1, 1):
                self.line = 8
                self.faceDir = 3
            case (-1, 1):
                self.line = 7
                self.faceDir = 5
            case (-1, -1):
                self.line = 2
                self.faceDir = 7
            case (1, -1):
                self.line = 3
                self.faceDir = 1
            case (0, 1):
                self.line = 6
                self.faceDir = 4
            case (0, -1):
                self.line = 1
                self.faceDir = 0
            case (1, 0):
                self.line = 5
                self.faceDir = 2
            case (-1, 0):
                self.line = 4
                self.faceDir = 6
            case (0, 0):
                self.add_event(STOP)

    def exit(self):
        print('Exit RUN')

    def do(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 6
        # move checking
        self.down = self.y - 35
        if self.dirX * self.dirY != 0:
            self.x += self.dirX * RUN_SPEED_PPS * game_framework.frame_time * (1 / math.sqrt(2)) * \
                        float(random.randint(8, 11) / 10)
            self.y += self.dirY * RUN_SPEED_PPS * game_framework.frame_time * (1 / math.sqrt(2)) * \
                      float(random.randint(8, 11) / 10)
        else:
            self.x += self.dirX * RUN_SPEED_PPS * game_framework.frame_time * float(random.randint(8, 11) / 10)
            self.y += self.dirY * RUN_SPEED_PPS * game_framework.frame_time * float(random.randint(8, 11) / 10)
        self.x = clamp(50, self.x, gamePlay.WIDTH - 50)
        self.y = clamp(20, self.y, gamePlay.HEIGHT - 20)
        rawTop = clamp(0, int(gamePlay.HEIGHT - self.y - gamePlay.mapstartY + 10) // gamePlay.boxSizeH,
                       len(gamePlay.mapping) - 1)
        rawBottom = clamp(0, int(gamePlay.HEIGHT - self.y - gamePlay.mapstartY - 10) // gamePlay.boxSizeH,
                          len(gamePlay.mapping) - 1)
        colLeft = clamp(0, int(self.x - gamePlay.mapstartX - 20) // gamePlay.boxSizeW, len(gamePlay.mapping[0]) - 1)
        colRight = clamp(0, int(self.x - gamePlay.mapstartX + 20) // gamePlay.boxSizeW, len(gamePlay.mapping[0]) - 1)
        if gamePlay.mapping[rawTop][colLeft] != 0 or gamePlay.mapping[rawTop][colRight] != 0 or \
                gamePlay.mapping[rawBottom][colLeft] != 0 or gamePlay.mapping[rawBottom][colRight] != 0:
            self.x = self.oldX
            self.y = self.oldY
        else:
            self.oldX = self.x
            self.oldY = self.y

        # moving camera
        if gamePlay.MAINMAP:
            if (0 < self.x - gamePlay.cameraLEFT < 300 and self.dirX < 0) or \
                    (1200 > self.x - gamePlay.cameraLEFT > 1200 - 300 and self.dirX > 0):
                if self.dirX * self.dirY != 0:
                    gamePlay.cameraLEFT += self.dirX * RUN_SPEED_PPS * game_framework.frame_time * (1 / math.sqrt(2))
                else:
                    gamePlay.cameraLEFT += self.dirX * RUN_SPEED_PPS * game_framework.frame_time
            elif (0 < self.y - gamePlay.cameraBOTTOM < 300 and self.dirY < 0) or \
                    (800 > self.y - gamePlay.cameraBOTTOM > 800 - 300 and self.dirY > 0):
                if self.dirX * self.dirY != 0:
                    gamePlay.cameraBOTTOM += self.dirY * RUN_SPEED_PPS * game_framework.frame_time * (1 / math.sqrt(2))
                else:
                    gamePlay.cameraBOTTOM += self.dirY * RUN_SPEED_PPS * game_framework.frame_time
            gamePlay.cameraLEFT = clamp(0, int(gamePlay.cameraLEFT), gamePlay.WIDTH - gamePlay.viewWIDTH)
            gamePlay.cameraBOTTOM = clamp(0, int(gamePlay.cameraBOTTOM), gamePlay.HEIGHT - gamePlay.viewHEIGHT)

        row = clamp(0,
                    int(gamePlay.HEIGHT - self.y - gamePlay.mapstartY) // gamePlay.boxSizeH + Looking[self.faceDir][0],
                    len(gamePlay.mapping) - 1)
        col = clamp(0, int(self.x - gamePlay.mapstartX) // gamePlay.boxSizeW + Looking[self.faceDir][1],
                    len(gamePlay.mapping[0]) - 1)
        self.bubbleCheck()
        if gamePlay.MAINMAP and gamePlay.mapping[row][col] == 2:
            game_framework.push_state(marketMap)
            self.x, self.y = 1736, gamePlay.HEIGHT - 100
        elif not gamePlay.MAINMAP and gamePlay.mapping[row][col] == 2:
            game_framework.pop_state()
            self.x, self.y = 2236, gamePlay.HEIGHT - 1516

    def draw(self):
        self.character.clip_draw(int(self.frame) * Pinn.pinnImageX,
                                 (2016 - Pinn.pinnImageY * (self.line + 1)),
                                 Pinn.pinnImageX, Pinn.pinnImageY,
                                 self.x - gamePlay.cameraLEFT,
                                 self.y + Pinn.pinnImageX / 2 - 20 - gamePlay.cameraBOTTOM)


class INTERACTION:
    def enter(self, event):
        print('Enter INTERACTION')
        self.line = 0
        if not gamePlay.MAINMAP:
            self.dirX = 0
            self.dirY = 0
        row = clamp(0,
                    int(gamePlay.HEIGHT - self.y - gamePlay.mapstartY) // gamePlay.boxSizeH + Looking[self.faceDir][0],
                    len(gamePlay.mapping) - 1)
        col = clamp(0, int(self.x - gamePlay.mapstartX) // gamePlay.boxSizeW + Looking[self.faceDir][1],
                    len(gamePlay.mapping[0]) - 1)
        something = gamePlay.mapping[row][col]

        match type(something):
            case objectClass.Store:
                something.marketUIopen()
            case marketClass.Table:
                something = something.sittingZombie
                if something.readyOrder:
                    # QueueTime.append(113)
                    something.orderCheck = True
                # 좀비가 wait 상태이고 컵을 플레이어가 들고있으면 평가들어감
                elif something.orderCheck and self.item == 'cup':
                    # 음료의 성공 여부를 좀비에게 전달.
                    # 음료의 성공 여부 작성.
                    self.cup = None
                    self.item = None
            case marketClass.waitingForSecond:
                if something.ready:
                    self.item = something.bubbleImage
                    something.ready = False
                elif not something.wait:
                    something.click()
            case marketClass.noWait:
                self.item = something.bubbleImage
                something.click()
            # case cupClass.Cup:
            #     if self.item != 'cup' and self.item is not None:
            #         something.putItem(self.item)
            #         self.item = None
            #     elif self.item is None:
            #         self.cup = something
            #         self.item = 'cup'
            #         mapping[self.cup.yIndex][self.cup.xIndex] = 1
            #         cups.remove(self.cup)
            #     elif self.item == 'cup':  # swap
            #         temp = something
            #         cups.remove(temp)
            #         self.cup.yIndex = raw
            #         self.cup.xIndex = col
            #         something = self.cup
            #         cups.append(self.cup)
            #         self.cup = temp
            # case objectClass.objectIndex:
            #     self.item = something.spacebar()
            #     if something in trashes:
            #         self.item = None
            #     if self.item == 'cup':
            #         self.cup.yIndex = raw
            #         self.cup.xIndex = col
            #         mapping[self.cup.yIndex][self.cup.xIndex] = self.cup
            #         cups.append(self.cup)
            #         self.cup = None
            #         self.item = None

    def exit(self):
        print('Exit INTERACTION')

    def do(self):
        pass

    def draw(self):
        self.character.clip_draw(self.faceDir * Pinn.pinnImageX,
                                 (2016 - Pinn.pinnImageY * (self.line + 1)),
                                 Pinn.pinnImageX, Pinn.pinnImageY,
                                 self.x - gamePlay.cameraLEFT,
                                 self.y + Pinn.pinnImageY / 2 - 45 - gamePlay.cameraBOTTOM)

next_state = {
    IDLE:  {RU: RUN,  LU: RUN,  RD: RUN, LD: RUN, NU: RUN, SU: RUN, ND: RUN, SD: RUN, SPACE: INTERACTION, STOP: IDLE},
    RUN:   {RU: RUN, LU: RUN, RD: RUN, LD: RUN, NU: RUN, SU: RUN, ND: RUN, SD: RUN, SPACE: INTERACTION, STOP: IDLE},
    INTERACTION: {RU: RUN, LU: RUN, RD: RUN, LD: RUN, NU: RUN, SU: RUN, ND: RUN, SD: RUN,
                  SPACE: INTERACTION, STOP: IDLE, ESC: IDLE},
}

PIXEL_PER_METER = 10.0 / 0.1
RUN_SPEED_KMPH = 20.0
RUN_SPEED_MPM = RUN_SPEED_KMPH * 1000.0 / 60.6
RUN_SPEED_MPS = RUN_SPEED_MPM / 60.0
RUN_SPEED_PPS = RUN_SPEED_MPS * PIXEL_PER_METER
TIME_PER_ACTION = 0.15
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 2

class Pinn:
    pinnImage = 'character1.6\\pinn.png'
    pinnImageX = 148
    pinnImageY = 224
    coffee = 'order\\bubble\\bean.png'
    blood = 'order\\bubble\\blood.png'
    milk = 'order\\bubble\\milkbubble.png'
    cupBubble = 'order\\bubble\\cup.png'
    myitems = [[None for i in range(6)] for j in range(6)]
    myitemList = []

    def __init__(self):
        self.character = load_image(Pinn.pinnImage)
        self.frame = 0
        self.x = gamePlay.WIDTH // 2 - 100
        self.y = gamePlay.HEIGHT // 2 - 100
        self.down = self.y - 35
        self.oldX = self.x
        self.oldY = self.y
        self.dirX = 0
        self.dirY = 0
        self.line = 0
        self.faceDir = 0
        self.item = None
        self.bubble = None
        self.something = None
        self.myInventory = marketClass.Inventory()
        self.inven = None
        self.event_que = []
        self.cur_state = IDLE
        self.cur_state.enter(self, None)

    def add_event(self, event):
        self.event_que.insert(0, event)

    def handle_events(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)


                # object = mapping[raw][col]

                # match type(object):
                #     case zombieClass.Zombie:
                #         if mapping[raw][col].cur_state == zombieClass.READY:
                #             menuQueue.append(mapping[raw][col].menu)
                #             QueueTime.append(113)
                #             mapping[raw][col].add_state(zombieClass.WAIT)
                #         #좀비가 wait 상태이고 컵을 플레이어가 들고있으면 평가들어감
                #         elif mapping[raw][col].cur_state == zombieClass.WAIT and \
                #             self.item == 'cup':
                #             # 음료의 성공 여부를 좀비에게 전달.
                #             mapping[raw][col].cur_state(self.cup.checkCup(mapping[raw][col].menu))
                #             self.cup = None
                #             self.item = None
                #     case cupClass.Cup:
                #         if self.item != 'cup' and self.item is not None:
                #             mapping[raw][col].putItem(self.item)
                #             self.item = None
                #         elif self.item is None:
                #             self.cup = mapping[raw][col]
                #             self.item = 'cup'
                #             mapping[self.cup.yIndex][self.cup.xIndex] = 1
                #             cups.remove(self.cup)
                #         elif self.item == 'cup':    # swap
                #             temp = mapping[raw][col]
                #             cups.remove(temp)
                #             self.cup.yIndex = raw
                #             self.cup.xIndex = col
                #             mapping[raw][col] = self.cup
                #             cups.append(self.cup)
                #             self.cup = temp
                #     case objectClass.objectIndex:
                #         self.item = mapping[raw][col].spacebar()
                #         if mapping[raw][col] in trashes:
                #             self.item = None
                #         if self.item == 'cup':
                #             self.cup.yIndex = raw
                #             self.cup.xIndex = col
                #             mapping[self.cup.yIndex][self.cup.xIndex] = self.cup
                #             cups.append(self.cup)
                #             self.cup = None
                #             self.item = None

    def draw(self):
        self.cur_state.draw(self)
        debug_print('PPPP')
        debug_print(f'Face Dir: {self.faceDir}, DirX: {self.dirX}, DirY: {self.dirY}')

        # if self.item is not None:
        #     match self.item:
        #         case 'shot':
        #             self.coffee.draw(self.x, self.y + 130)
        #         case 'blood':
        #             self.blood.draw(self.x, self.y + 130)
        #         case 'milk':
        #             self.milk.draw(self.x, self.y + 130)
        #         case 'cup':
        #             self.cupBubble.draw(self.x, self.y + 140)

        # 입체감

    def bubbleCheck(self):
        # bubble checking
        row = clamp(0,
                    int(gamePlay.HEIGHT - self.y - gamePlay.mapstartY) // gamePlay.boxSizeH + Looking[self.faceDir][0],
                    len(gamePlay.mapping) - 1)
        col = clamp(0, int(self.x - gamePlay.mapstartX) // gamePlay.boxSizeW + Looking[self.faceDir][1],
                    len(gamePlay.mapping[0]) - 1)
        something = gamePlay.mapping[row][col]
        if something != self.something:
            if self.bubble is not None:
                AllObjectClass.remove_object(self.bubble)
                self.bubble = None
            else:
                match type(something):
                    case marketClass.noWait:
                        self.bubble = objectClass.Bubble(*something.cur_state.makeBubble(something))
                        AllObjectClass.add_object(self.bubble, 2)
                    case marketClass.waitingForSecond:
                        if not something.wait and not something.ready:
                            self.bubble = objectClass.Bubble(*something.cur_state.makeBubble(something))
                            AllObjectClass.add_object(self.bubble, 2)
                    case objectClass.Store:
                        self.bubble = objectClass.Bubble(*something.makeBubble())
                        AllObjectClass.add_object(self.bubble, 2)
        self.something = something

    def update(self):
        self.cur_state.do(self)
        if self.event_que:
            event = self.event_que.pop()
            self.cur_state.exit(self)
            try:
                self.cur_state = next_state[self.cur_state][event]
            except KeyError:
                # print(f'Error: State {self.cur_state.__name__}    Event{event_name[event]}')
                print('ERROR', self.cur_state.__name__, ' ', event_name[event])
            self.cur_state.enter(self, event)

    def InventoryTest(self):
        if self.inven:
            AllObjectClass.add_object(self.inven, 6)

    def InventoryRemove(self):
        if self.inven != None:
            AllObjectClass.remove_object(self.inven)
            self.inven = None
