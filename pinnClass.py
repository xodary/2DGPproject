import random

import animalRoomFramework
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
            self.ComeonInven()

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
            self.ComeonInven()
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
        self.woodFloor.set_volume(0)
        self.concreteFloor.set_volume(0)
        self.animalRoom.set_volume(0)

    def do(self):
        if not gamePlay.animalRoom:
            if gamePlay.MAINMAP:
                if 1060 < self.x < 1060 + 900 and 600 < self.y < 1100:
                    self.woodFloor.set_volume(50)
                    self.concreteFloor.set_volume(0)
                else:
                    self.woodFloor.set_volume(0)
                    self.concreteFloor.set_volume(50)
            else:
                self.woodFloor.set_volume(0)
                self.concreteFloor.set_volume(50)
        else:
            self.animalRoom.set_volume(50)
            self.concreteFloor.set_volume(0)
            self.woodFloor.set_volume(0)

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
        if gamePlay.animalRoom:
            self.x = clamp(animalRoomFramework.left, self.x, animalRoomFramework.right)
            self.y = clamp(animalRoomFramework.bottom, self.y, animalRoomFramework.top)
            rawTop = clamp(0, int(animalRoomFramework.top - self.y + 10) // gamePlay.boxSizeH, 6)
            rawBottom = clamp(0, int(animalRoomFramework.top - self.y - 10) // gamePlay.boxSizeH, 6)
            colLeft = clamp(0, int(self.x - animalRoomFramework.left - 10) // gamePlay.boxSizeW, 15)
            colRight = clamp(0, int(self.x - animalRoomFramework.left + 10) // gamePlay.boxSizeW, 15)
        else:
            self.x = clamp(50, self.x, gamePlay.WIDTH - 50)
            self.y = clamp(20, self.y, gamePlay.HEIGHT - 20)
            rawTop = clamp(0, int(gamePlay.HEIGHT - self.y - gamePlay.mapstartY + 10) // gamePlay.boxSizeH,
                           len(gamePlay.mapping) - 1)
            rawBottom = clamp(0, int(gamePlay.HEIGHT - self.y - gamePlay.mapstartY - 10) // gamePlay.boxSizeH,
                              len(gamePlay.mapping) - 1)
            colLeft = clamp(0, int(self.x - gamePlay.mapstartX - 20) // gamePlay.boxSizeW, len(gamePlay.mapping[0]) - 1)
            colRight = clamp(0, int(self.x - gamePlay.mapstartX + 20) // gamePlay.boxSizeW,
                             len(gamePlay.mapping[0]) - 1)
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
        if gamePlay.MAINMAP and gamePlay.mapping[row][col] == 3:
            game_framework.push_state(animalRoomFramework)
        elif not gamePlay.MAINMAP and gamePlay.animalRoom and gamePlay.mapping[rawBottom][colRight] == 3:
            game_framework.pop_state()
            self.x, self.y = 1300, 1200

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
        if event == INVEN:
            self.ComeonInven()
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
                if not something.sittingZombie:
                    return
                something = something.sittingZombie
                if something.readyOrder:
                    # QueueTime.append(113)
                    something.orderCheck = True
                # 좀비가 wait 상태이고 컵을 플레이어가 들고있으면 평가들어감
                elif something.orderCheck and self.item == 'bubble\\cup.png':
                    # 음료의 성공 여부를 좀비에게 전달.
                    if self.cup.checkCup(something.menu):
                        something.success = True
                    else:
                        something.fail = True
                    self.cup = None
                    self.item = None
            case marketClass.waitingForSecond:
                if something.ready and not self.item:
                    self.item = something.bubbleImage
                    something.ready = False
                elif not something.wait:
                    something.click()
            case marketClass.noWait:
                if not self.item:
                    self.item = something.bubbleImage
                    something.click()
                    if something.furnitureImage == 'map1.6\\cuptableSmall.png':
                        self.cup = cupClass.Cup()

            case cupClass.Cup:
                if self.item != 'bubble\\cup.png' and self.item:
                    something.putItem(self.item)
                    self.item = None
                elif self.item != 'bubble\\cup.png' and not self.item:
                    self.cup = something
                    self.item = 'bubble\\cup.png'
                    for n in range(3):
                        gamePlay.mapping[self.cup.yIndex][self.cup.xIndex - 1 + n] = self.tempTableInform
                    gamePlay.furnitureList.remove(self.cup)
                    AllObjectClass.remove_object(self.cup)
                elif self.item == 'bubble\\cup.png':  # swap
                    gamePlay.furnitureList.remove(something)
                    AllObjectClass.remove_object(something)
                    self.cup.yIndex = something.yIndex
                    self.cup.xIndex = something.xIndex
                    gamePlay.furnitureList.append(self.cup)
                    AllObjectClass.add_object(self.cup, 1)
                    for n in range(3):
                        gamePlay.mapping[self.cup.yIndex][self.cup.xIndex - 1 + n] = self.cup
                    self.cup = something

            case marketClass.Myitem:
                if something.furnitureImage == 'map1.6\\trash.png':
                    self.item = None
                    return
                if something.furnitureImage == 'map1.6\\kitchenTable.png':
                    if self.item != 'bubble\\cup.png':
                        for n in range(3):
                            if type(gamePlay.mapping[row][col - 1 + n]) == cupClass.Cup:
                                something = gamePlay.mapping[row][col - 1 + n]

                                if self.item != 'bubble\\cup.png' and self.item:
                                    something.putItem(self.item)
                                    self.item = None
                                elif self.item != 'bubble\\cup.png' and not self.item:
                                    self.cup = something
                                    self.item = 'bubble\\cup.png'
                                    for a in range(3):
                                        gamePlay.mapping[self.cup.yIndex][
                                            self.cup.xIndex - 1 + a] = self.tempTableInform
                                    gamePlay.furnitureList.remove(self.cup)
                                    AllObjectClass.remove_object(self.cup)
                                elif self.item == 'bubble\\cup.png':  # swap
                                    gamePlay.furnitureList.remove(something)
                                    AllObjectClass.remove_object(something)
                                    self.cup.yIndex = something.yIndex
                                    self.cup.xIndex = something.xIndex
                                    gamePlay.furnitureList.append(self.cup)
                                    AllObjectClass.add_object(self.cup, 1)
                                    for a in range(3):
                                        gamePlay.mapping[self.cup.yIndex][self.cup.xIndex - 1 + a] = self.cup
                                    self.cup = something
                        return

                    for n in range(3):
                        if type(gamePlay.mapping[row][col - 1 + n]) != marketClass.Myitem or \
                                gamePlay.mapping[row][col - 1 + n].furnitureImage != 'map1.6\\kitchenTable.png':
                            return
                    self.cup.yIndex = row
                    self.cup.xIndex = col
                    self.tempTableInform = something
                    self.cup.down = self.tempTableInform.down - 1
                    gamePlay.mapping[self.cup.yIndex][self.cup.xIndex] = self.cup
                    gamePlay.furnitureList.append(self.cup)
                    AllObjectClass.add_object(self.cup, 1)
                    self.cup = None
                    self.item = None

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
    IDLE: {RU: RUN, LU: RUN, RD: RUN, LD: RUN, NU: RUN, SU: RUN, ND: RUN, SD: RUN, SPACE: INTERACTION, STOP: IDLE},
    RUN: {RU: RUN, LU: RUN, RD: RUN, LD: RUN, NU: RUN, SU: RUN, ND: RUN, SD: RUN, SPACE: INTERACTION, STOP: IDLE},
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
        self.woodFloor = load_wav('sound\\footWood.wav')
        self.woodFloor.repeat_play()
        self.woodFloor.set_volume(0)
        self.concreteFloor = load_wav('sound\\footConcrete.wav')
        self.concreteFloor.repeat_play()
        self.concreteFloor.set_volume(0)
        self.animalRoom = load_wav('sound\\animalRoom.wav')
        self.animalRoom.repeat_play()
        self.animalRoom.set_volume(0)
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
        self.money = 10

    def add_event(self, event):
        self.event_que.insert(0, event)

    def handle_events(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)


    def draw(self):
        self.cur_state.draw(self)
        if self.item:
            drawingBubble = load_image(self.item)
            drawingBubble.clip_draw(0, 0, 100, 100,
                                    self.x - gamePlay.cameraLEFT,
                                    self.y + 220 - gamePlay.cameraBOTTOM)

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

    def ComeonInven(self):
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
