import std
from std import *
from pico2d import *
import gamePlay
import game_framework

class interactionTOOL:
    def __init__(self, xIndex, yIndex, wIndex, hIndex, width, height,
                 pngName, bubbleimage=None, bubbleSize=100):
        self.image = load_image(pngName)
        self.xIndex = xIndex + gamePlay.MainMapPlusX
        self.yIndex = yIndex + gamePlay.MainMapPlusY
        # x와 y는 정가운데임.
        self.x = gamePlay.mapstartX + gamePlay.boxSizeW * self.xIndex + gamePlay.boxSizeW * wIndex / 2
        self.width, self.height = width, height
        self.y = gamePlay.HEIGHT - (gamePlay.mapstartY + gamePlay.boxSizeH * self.yIndex + gamePlay.boxSizeH * hIndex - self.height / 2)
        self.down = self.y - self.height / 2
        self.bubbleimage = bubbleimage
        self.bubbleSize = bubbleSize
        global mapping
        for i in range(wIndex):
            for j in range(hIndex):
                gamePlay.mapping[self.yIndex + j][self.xIndex + i] = self

    def __lt__(self, otherObj):
        return self.image < otherObj.image

    def update(self):
        pass

    def makeBubble(self):
        return self.x, self.y + self.height / 2 + 60, self.bubbleimage, self.bubbleSize

    def draw(self):
        self.image.draw(self.x - gamePlay.cameraLEFT, self.y - gamePlay.cameraBOTTOM)
        # self.image.draw(self.x, self.y)

class Bubble:
    makingBubble = 'bubble\\makebubble.png'
    TIME_PER_ACTION = 0.2
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 4
    def __init__(self, x, y, itemBubble, size):
        self.make = load_image(Bubble.makingBubble)
        self.image = load_image(itemBubble)
        self.size = size
        self.x = x
        self.y = y
        self.frame = 0
        self.makingframe = 0
    def draw(self):
        if self.makingframe < 3:
            self.make.clip_draw(self.size * int(self.makingframe), 0, self.size,
                                      self.size, self.x - gamePlay.cameraLEFT, self.y - gamePlay.cameraBOTTOM)
        else:
            self.image.clip_draw(self.size * (int(self.frame) // 4), 0, self.size,
                             self.size, self.x - gamePlay.cameraLEFT, self.y - gamePlay.cameraBOTTOM)
    def update(self):
        if self.makingframe < 3:
            self.makingframe += (self.frame + Bubble.FRAMES_PER_ACTION * Bubble.ACTION_PER_TIME * game_framework.frame_time)
        else:
            self.frame = (self.frame + Bubble.FRAMES_PER_ACTION * Bubble.ACTION_PER_TIME * game_framework.frame_time) % 16

class WALL:
    def __init__(self, x, y, width, height, pngName):
        self.image = load_image(pngName)
        self.width, self.height = width, height
        self.x = x + self.width / 2
        self.y = gamePlay.HEIGHT - (y + self.height / 2)
        self.down = self.y - self.height // 2

    def __lt__(self, otherObj):
        return self.image < otherObj.image
    def update(self):
        pass

    def draw(self):
        self.image.draw(self.x - gamePlay.cameraLEFT, self.y - gamePlay.cameraBOTTOM)
        # self.image.draw(self.x, self.y)
class BackGround:
    def __init__(self, pngName):
        self.image = load_image(pngName)
    def __lt__(self, otherObj):
        return self.image < otherObj.image
    def update(self):
        pass
    def draw(self):
        self.image.clip_draw(gamePlay.cameraLEFT, gamePlay.cameraBOTTOM,
                             gamePlay.viewWIDTH, gamePlay.viewHEIGHT,
                             gamePlay.viewWIDTH // 2, gamePlay.viewHEIGHT // 2)
class TABLE(interactionTOOL):
    def __init__(self, xIndex, yIndex, wIndex, hIndex, width, height, pngName, itemBubble=None, bubbleSize=80):
        super().__init__(xIndex, yIndex, wIndex, hIndex, width, height, pngName, itemBubble, bubbleSize)
        self.sit = False

    def update(self):
        pass

    def SIT(self):
        self.sit = True

    def WAKEUP(self):
        self.sit = False

    def CHECKTABLE(self):
        return self.sit
    def draw(self):
        self.image.draw(self.x - gamePlay.cameraLEFT, self.y - gamePlay.cameraBOTTOM)
        # self.image.draw(self.x, self.y)

class fire(WALL):
    TIME_PER_ACTION = 0.2
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 4
    def __init__(self, x, y, width, height, pngName):
        super().__init__(x, y, width, height, pngName)
        self.frame = 0

    def __lt__(self, otherObj):
        return self.image < otherObj.image

    def update(self):
        self.frame = (self.frame + fire.FRAMES_PER_ACTION * fire.ACTION_PER_TIME * game_framework.frame_time) % 16


    def draw(self):
        self.image.clip_draw((int(self.frame) // 4) * self.width, 0, self.width, self.height,
                             self.x - gamePlay.cameraLEFT, self.y - gamePlay.cameraBOTTOM)


