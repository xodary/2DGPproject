from pico2d import *
import gamePlay
import marketFramework
import pinnClass

myitems = [
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
    ]
class marketUI:
    def __init__(self):
        self.image = load_image('UI\\marketUI.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(gamePlay.viewWIDTH // 2, gamePlay.viewHEIGHT // 2)
        for items in myitems:
            for item in items:
                if type(item) == miniMarket:
                    item.draw()

class marketSell:
    def __init__(self, pngName, miniM, miniI, left, top, width, height, weightX, weightY):
        self.image = load_image(pngName)
        self.miniI = miniI
        self.miniM = miniM
        self.x = left + width / 2
        self.y = gamePlay.HEIGHT - (top + height / 2)
        self.width = width
        self.height = height
        self.weightX = weightX
        self.weightY = weightY
        self.MouseOn = False


    def update(self):
        pass

    def mouseOn(self):
        if not self.MouseOn:
            self.MouseOn = True
    def mouseOff(self):
        if self.MouseOn:
            self.MouseOn = False

    def makeMarket(self, x, y):
        return miniMarket(self.miniM, self.miniI, x, y, self.weightX, self.weightY)
    def draw(self):
        if self.MouseOn:
            self.image.draw(self.x, self.y)
        else:
            self.image.clip_draw(8, 8, self.width - 16, self.height - 16, self.x, self.y)

class miniMarket:
    width = 120
    height = 114
    imageW = 103
    imageH = 103
    left = 1045
    top = 270
    def __init__(self, pngName, itemImage, x, y, weightX, weightY, xIndex=0, yIndex = 0):
        self.image = load_image(pngName)
        self.item = itemImage
        self.x = x
        self.y = y
        self.weightX = weightX
        self.weightY = weightY
        self.fit = False
        self.xIndex = xIndex
        self.yIndex = yIndex

    def update(self):
        pass

    def draw(self):
        if not self.fit:
            self.image.draw(self.x, self.y)
        else:
            self.image.draw(miniMarket.left + (self.xIndex + self.weightX - 1) * miniMarket.width + miniMarket.imageW / 2,
                            gamePlay.HEIGHT - (miniMarket.top + (self.yIndex + self.weightY - 1) * miniMarket.height + miniMarket.imageH / 2))

    def mouseOffTest(self):
        xCenter = (self.x - miniMarket.left) // self.width
        yCenter = (gamePlay.HEIGHT - self.y - miniMarket.top) // self.height
        self.xIndex = xCenter - self.weightX // 2
        self.yIndex = yCenter - self.weightY // 2
        if 0 <= xCenter <= 5 and 0 <= yCenter <= 5 and 0 <= self.xIndex <= 5 and 0 <= self.yIndex <= 5:
            for y in range(self.weightY):
                for x in range(self.weightX):
                    if myitems[self.yIndex + y][self.xIndex + x] != 0:
                        return False
        else:
            return False

        return True

    def success(self):
        for y in range(self.weightY):
            for x in range(self.weightX):
                myitems[self.yIndex + y][self.xIndex + x] = 1
        myitems[self.yIndex][self.xIndex] = self
        self.fit = True
    def makeMiniInven(self):
        return self.item, self.xIndex, self.yIndex, self.weightX, self.weightY



class Inventory:
    image = 'UI\\itemUI.png'
    ImageW = 176 * 4
    ImageH = 197 * 4
    width = 176 * 4
    height = 197 * 4

    def __init__(self):
        self.image = load_image(Inventory.image)
        self.ImageW = Inventory.ImageW
        self.ImageH = Inventory.ImageH
        self.width = Inventory.width
        self.height = Inventory.height
        self.x = gamePlay.viewWIDTH - self.width // 2
        self.y = self.height // 2


    def update(self):
        pass

    def draw(self):
        self.image.clip_draw(0, 0, self.ImageW, self.ImageH, self.x, self.y, self.width, self.height)
        for items in myitems:
            for item in items:
                if type(item) is miniMarket:
                    miniInven(*item.makeMiniInven()).draw()

class miniInven:
    itemUIleft, itemUItop = 1920 - Inventory.width, Inventory.height
    left, top = 108, 160
    width, height = 84, 80
    imageW, imageH = 72, 72
    diffW = 12
    diffH = 8
    def __init__(self, image, leftIndex, topIndex, weightX, weightY):
        self.image = load_image(image)
        self.leftIndex, self.topIndex = leftIndex, topIndex
        self.weightX, self.weightY = weightX, weightY
        self.x, self.y = miniInven.itemUIleft + miniInven.left + self.leftIndex * miniInven.width + (self.weightX * miniInven.width - miniInven.diffW) // 2, \
                         miniInven.itemUItop - (miniInven.top + self.topIndex * miniInven.height + (self.weightY * miniInven.height - miniInven.diffH) // 2)

    def update(self):
        pass

    def draw(self):
        self.image.draw(self.x, self.y)