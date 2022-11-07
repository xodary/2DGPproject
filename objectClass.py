import std
from std import *
from pico2d import *
import gamePlay

class interactionTOOL:
    def __init__(self, xIndex, yIndex, wIndex, hIndex, width, height,
                 pngName, bubbleimage=None, bubbleSize=100, bubbleframe=0):
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
        self.bubbleframe = bubbleframe
        global mapping
        for i in range(wIndex):
            for j in range(hIndex):
                gamePlay.mapping[self.yIndex + j][self.xIndex + i] = self

    def __lt__(self, otherObj):
        return self.image < otherObj.image

    def update(self):
        pass


    def draw(self):
        self.image.draw(self.x - gamePlay.cameraLEFT, self.y - gamePlay.cameraBOTTOM)
        # self.image.draw(self.x, self.y)

class Bubble:
    makingBubble = 'bubble\\makebubble.png'
    def __init__(self, x, y, itemBubble, size, frame):
        self.make = load_image(Bubble.makingBubble)
        self.image = load_image(itemBubble)
        self.size = size
        self.x = x
        self.y = y
        self.MaxFrame = frame
        self.frame = 0
        self.makingframe = 0
    def draw(self):
        if self.makingframe < 3:
            self.make.clip_draw(self.size * self.makingframe, 0, self.size,
                                      self.size, self.x - gamePlay.cameraLEFT, self.y - gamePlay.cameraBOTTOM)
        else:
            self.image.clip_draw(self.size * (self.frame // 4), 0, self.size,
                             self.size, self.x - gamePlay.cameraLEFT, self.y - gamePlay.cameraBOTTOM)
    def update(self):
        if self.makingframe < 3:
            self.makingframe += 1
        else:
            self.frame = (self.frame + 1) % 16

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
        self.image.clip_draw(gamePlay.cameraLEFT, gamePlay.cameraBOTTOM, gamePlay.viewWIDHT, gamePlay.viewHEIGHT, gamePlay.viewWIDHT / 2, gamePlay.viewHEIGHT / 2)
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
    def __init__(self, x, y, width, height, pngName):
        super().__init__(x, y, width, height, pngName)
        self.frame = 0

    def __lt__(self, otherObj):
        return self.image < otherObj.image

    def update(self):
        self.frame = (self.frame + 1) % 16

    def draw(self):
        self.image.clip_draw((self.frame // 4) * self.width, 0, self.width, self.height,
                             self.x - gamePlay.cameraLEFT, self.y - gamePlay.cameraBOTTOM)


