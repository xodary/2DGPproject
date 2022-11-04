import std
from std import *
from pico2d import *


class interactionTOOL:
    def __init__(self, xIndex, yIndex, wIndex, hIndex, width, height, pngName, bubbleimage=None, bubbleSize=50):
        self.image = load_image(pngName)
        self.xIndex = xIndex + 18
        self.yIndex = yIndex + 9
        # x와 y는 정가운데임.
        self.x = mapstartX + boxSizeW * self.xIndex + boxSizeW * wIndex / 2
        self.width, self.height = width, height
        self.y = HEIGHT - (mapstartY + boxSizeH * self.yIndex + boxSizeH * hIndex - self.height / 2)
        self.down = self.y - self.height / 2
        self.bubbleimage = bubbleimage
        self.bubbleSize = bubbleSize
        for i in range(wIndex):
            for j in range(hIndex):
                mapping[self.yIndex + j][self.xIndex + i] = self

    def __lt__(self, otherObj):
        return self.image < otherObj.image

    def update(self):
        pass

    def GetBubble(self):
        if self.bubbleimage is not None:
            return self.x, self.y + self.height / 2 + 30, self.bubbleimage, self.bubbleSize

    def draw(self):
        self.image.draw(self.x - std.cameraLEFT, self.y - std.cameraBOTTOM)
        # self.image.draw(self.x, self.y)

class Bubble:
    def __init__(self, x, y, itemBubble, size):
        self.image = load_image(itemBubble)
        self.size = size
        self.x = x
        self.y = y
        self.frame = 0
    def draw(self):
        self.image.clip_draw(self.size * self.frame, 0, self.size,
                                      self.size, self.x - std.cameraLEFT, self.y - std.cameraBOTTOM)
        # self.image.clip_draw(self.size * self.frame, 0, self.size,
        #                      self.size, self.x, self.y)
    def update(self):
        if self.frame < 2:
            self.frame += 1

class WALL:
    def __init__(self, x, y, width, height, pngName):
        self.image = load_image(pngName)
        self.width, self.height = width, height
        self.x = x + self.width / 2
        self.y = HEIGHT - (y + self.height / 2)
        self.down = self.y - self.height // 2

    def __lt__(self, otherObj):
        return self.image < otherObj.image
    def update(self):
        pass

    def draw(self):
        self.image.draw(self.x - std.cameraLEFT, self.y - std.cameraBOTTOM)
        # self.image.draw(self.x, self.y)
class BackGround:
    def __init__(self, pngName):
        self.image = load_image(pngName)
    def __lt__(self, otherObj):
        return self.image < otherObj.image
    def update(self):
        pass
    def draw(self):
        self.image.clip_draw(std.cameraLEFT, std.cameraBOTTOM, std.viewWIDHT, std.viewHEIGHT, std.viewWIDHT / 2, std.viewHEIGHT / 2)
class TABLE(interactionTOOL):
    def __init__(self, xIndex, yIndex, wIndex, hIndex, width, height, pngName, itemBubble=None, bubbleSize=50):
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
        self.image.draw(self.x - std.cameraLEFT, self.y - std.cameraBOTTOM)
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
        self.image.clip_draw((self.frame // 4) * 40, 0, 40, 70, self.x - std.cameraLEFT, self.y - std.cameraBOTTOM)


