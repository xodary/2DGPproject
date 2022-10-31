from std import *
from pico2d import *


class objectIndex:
    def __init__(self, xIndex, yIndex, wIndex, hIndex, width, height, pngName, itemBubble=None, bubbleSize=50):
        self.image = load_image(pngName)
        self.xIndex = xIndex + 1
        self.yIndex = yIndex + 1
        # x와 y는 정가운데임.
        self.x = mapstartX + boxSizeW * self.xIndex + boxSizeW * wIndex / 2
        self.width, self.height = width, height
        self.y = HEIGHT - (mapstartY + boxSizeH * self.yIndex + boxSizeH * hIndex - self.height / 2)
        self.down = self.y - self.height / 2
        self.bubbleSize = bubbleSize
        self.itemBubble = None
        if itemBubble is not None:
            self.itemBubble = load_image(itemBubble)
        self.bubbleY = self.y + self.height / 2 + 30
        for i in range(wIndex):
            for j in range(hIndex):
                mapping[self.yIndex + j][self.xIndex + i] = self

    def __lt__(self, otherObj):
        return self.image < otherObj.image

    def drawBubble(self, frame):
        if self.itemBubble is not None:
            self.itemBubble.clip_draw(self.bubbleSize * frame, 0, self.bubbleSize,
                                      self.bubbleSize, self.x, self.bubbleY)

    def spacebar(self):
        if self.itemBubble is not None:
            return self.itemBubble

    def draw(self):
        self.image.draw(self.x, self.y)


class objectCoordi:
    def __init__(self, x, y, width, height, pngName):
        self.image = load_image(pngName)
        self.width, self.height = width, height
        self.x = x + self.width / 2
        self.y = HEIGHT - (y + self.height / 2)
        self.down = self.y - self.height // 2

    def __lt__(self, otherObj):
        return self.image < otherObj.image


    def draw(self):
        self.image.draw(self.x, self.y)


class TABLE(objectIndex):
    def __init__(self, xIndex, yIndex, wIndex, hIndex, pngName):
        super().__init__(xIndex, yIndex, wIndex, hIndex, pngName)
        self.sit = False

    def SIT(self):
        self.sit = True

    def WAKEUP(self):
        self.sit = False

    def CHECKTABLE(self):
        return self.sit
