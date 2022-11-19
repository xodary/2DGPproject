from pico2d import *
import gamePlay
import marketFramework
import pinnClass
import AllObjectClass


class MarketUI_Background:
    menuL, menuR, menuB, menuT = 189, 189 + 700, 1280 - (270 + 695), 1920 - 270
    itemL, itemR, itemB, itemT = 1041, 1041 + 707, 1280 - (270 + 678), 1920 - 270

    def __init__(self):
        self.image = load_image('UI\\marketUI.png')
        self.items = None
        self.buttons = None
        self.buttonNum = 0

    def update(self):
        pass

    def draw(self):
        self.image.draw(gamePlay.viewWIDTH // 2, gamePlay.viewHEIGHT // 2)
        for a in pinnClass.Pinn.myitems:
            for b in a:
                for c in b:
                    if type(c) == Myitem:
                        c.makeBigIcon().draw()

    def GetItems(self, items, buttons):
        self.items = items
        self.buttons = buttons
        AllObjectClass.add_objects(self.items[self.buttonNum], 5)

    def MouseButtonDown(self, x, y):
        # push button
        for button in self.buttons:
            if button.mouseOn(x, y, self.buttonNum):
                self.buttons[self.buttonNum].mouseOff()
                for order in self.items[self.buttonNum]:
                    AllObjectClass.remove_object(order)
                self.buttonNum = button.returnButton()
                AllObjectClass.add_objects(self.items[self.buttonNum], 5)
        # menu 칸에 클릭하면 선택함
        for item in self.items[self.buttonNum]:
            if item.mouseTest(x, y):
                return item.makeBigIcon(x, y)
        return None

    def MouseMotion(self, x, y, mouseOn):
        for Button in self.buttons:
            Button.mouseOn(x, y, self.buttonNum)
        if mouseOn:
            # item 쪽에 마우스 올리면 칸에 쏙 들어감
            if MarketUI_Background.itemL <= x <= MarketUI_Background.itemR and \
                    MarketUI_Background.itemB <= y <= MarketUI_Background.itemT:
                if mouseOn.mouseOffTest():
                    mouseOn.fitOn()
                else:
                    mouseOn.fitOff()
            else:
                mouseOn.fitOff()
        for item in self.items[self.buttonNum]:
            if item.mouseTest(x, y):
                item.mouseOn()
            else:
                item.mouseOff()

    def MouseButtonUp(self, mouseOn):
        if mouseOn:
            if mouseOn.mouseOffTest():
                mouseOn.success()
                marketFramework.itemImages.append(mouseOn)
            else:
                AllObjectClass.remove_object(mouseOn)
    def exit(self):
        for item in self.items[self.buttonNum]:
            AllObjectClass.remove_object(item)

class OrderBox:
    def __init__(self, pngName, BigIcon, SmallIcon, left, top, width, height,
                 weightX, weightY, weightMapX, weightMapY, weightList=None, weightMapList=None):
        self.image = load_image(pngName)
        self.BigIcon = BigIcon
        self.SmallIcon = SmallIcon
        self.x, self.y = left + width / 2, gamePlay.HEIGHT - (top + height / 2)
        self.width, self.height = width, height
        self.weightX, self.weightY = weightX, weightY
        self.weightMapX, self.weightMapY = weightMapX, weightMapY
        self.MouseOn = False
        if weightList:
            self.weightList = weightList
        else:
            self.weightList = [[1 for i in range(weightX)] for j in range(weightY)]
        if weightMapList:
            self.weightMapList = weightMapList
        else:
            self.weightMapList = [[1 for i in range(weightMapX)] for j in range(weightMapY)]

    def update(self):
        pass

    def mouseOn(self):
        self.MouseOn = True

    def mouseOff(self):
        self.MouseOn = False

    def mouseTest(self, x, y):
        if self.x - self.width / 2 < x < self.x + self.width / 2 and \
                self.y - self.height / 2 < y < self.y + self.height / 2:
            return True
        return False

    def makeBigIcon(self, x, y):
        icon = BigIcon(self.BigIcon, self.SmallIcon, x, y,
                       self.weightX, self.weightY, self.weightMapX, self.weightMapY,
                       self.weightList, self.weightMapList)
        AllObjectClass.add_object(icon, 6)
        return icon

    def draw(self):
        if self.MouseOn:
            self.image.draw(self.x, self.y)
        else:
            self.image.clip_draw(8, 8, self.width - 16, self.height - 16, self.x, self.y)


class Myitem:
    def __init__(self, Big, Small, xindex, yindex, weightX, weightY, weightMapX, weightMapY, weightList, weightMapList):
        self.big = Big
        self.small = Small
        self.weightX, self.weightY = weightX, weightY
        self.weightMapX, self.weightMapY = weightMapX, weightMapY
        self.xindex, self.yindex = xindex, yindex
        self.weightList = weightList
        self.weightMapList = weightMapList
    def update(self):
        pass

    def draw(self):
        pass

    def makeBigIcon(self):
        return BigIcon(self.big, self.small, 0, 0, self.weightX, self.weightY, self.weightMapX, self.weightMapY,
                       self.weightList, self.weightMapList, self.xindex, self.yindex, True)

    def makeSmallIcon(self):
        return SmallIcon(self.small, self.xindex, self.yindex, self.weightX, self.weightY,
                         self.weightMapX, self.weightMapY, self.weightList, self.weightMapList)


class BigIcon:
    width = 118
    height = 114
    imageW = 108
    imageH = 108
    left = 1041
    top = 270
    diffW = 10
    diffH = 6

    def __init__(self, pngName, smallIcon, x, y,
                 weightX, weightY, weightMapX, weightMapY,
                 weightList, weightMapList,
                 xIndex=0, yIndex=0, fit=False):
        self.image = load_image(pngName)
        self.BigIcon = pngName
        self.SmallIcon = smallIcon
        self.x, self.y = x, y
        self.weightX, self.weightY = weightX, weightY
        self.weightMapX, self.weightMapY = weightMapX, weightMapY
        self.fit = fit
        self.xIndex, self.yIndex = xIndex, yIndex
        self.weightList = weightList
        self.weightMapList = weightMapList

    def update(self):
        if not self.fit:
            self.x, self.y = marketFramework.x, marketFramework.y

    def draw(self):
        if not self.fit:
            self.image.draw(self.x, self.y)
        else:
            self.image.draw(BigIcon.left + self.xIndex * BigIcon.width +
                            (self.weightX * BigIcon.width - BigIcon.diffW) // 2,
                            gamePlay.HEIGHT - (BigIcon.top + self.yIndex * BigIcon.height +
                                               (self.weightY * BigIcon.height - BigIcon.diffH) // 2))

    def mouseOffTest(self):
        xCenter = (self.x - BigIcon.left)
        yCenter = (gamePlay.HEIGHT - self.y - BigIcon.top)
        self.xIndex = int(xCenter - self.weightX / 2 * BigIcon.imageW) // BigIcon.imageW
        self.yIndex = int(yCenter - self.weightY / 2 * BigIcon.imageH) // BigIcon.imageH
        print(self.xIndex, self.yIndex)
        if 0 <= self.xIndex <= 5 and 0 <= self.yIndex <= 5 and \
                0 <= self.xIndex + self.weightX - 1 <= 5 and 0 <= self.yIndex + self.weightY - 1 <= 5:
            for y in range(self.weightY):
                for x in range(self.weightX):
                    if self.weightList[y][x] == 1:
                        if 1 in pinnClass.Pinn.myitems[self.yIndex + y][self.xIndex + x]:
                            return False
        else:
            return False
        return True

    def success(self):
        for y in range(self.weightY):
            for x in range(self.weightX):
                if self.weightList[y][x] == 1:
                    pinnClass.Pinn.myitems[self.yIndex + y][self.xIndex + x].append(1)
        pinnClass.Pinn.myitems[self.yIndex][self.xIndex].append(Myitem(self.BigIcon, self.SmallIcon,
                                                                  self.xIndex, self.yIndex,
                                                                  self.weightX, self.weightY,
                                                                  self.weightMapX, self.weightMapY,
                                                                  self.weightList, self.weightMapList))
        self.fit = True

    def fitOn(self):
        self.fit = True

    def fitOff(self):
        self.fit = False


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
        for a in pinnClass.Pinn.myitems:
            for b in a:
                for c in b:
                    if type(c) is Myitem:
                        c.makeSmallIcon().draw()


class SmallIcon:
    itemUIleft, itemUItop = 1920 - Inventory.width, Inventory.height
    left, top = 104, 160
    width, height = 84, 80
    imageW, imageH = 76, 76
    diffW = 8
    diffH = 4

    def __init__(self, image, leftIndex, topIndex, weightX, weightY, weightMapX, weightMapY, weightList, weightMapList):
        self.image = load_image(image)
        self.leftIndex, self.topIndex = leftIndex, topIndex
        self.weightX, self.weightY = weightX, weightY
        self.weightMapX, self.weightMapY = weightMapX, weightMapY
        self.x = SmallIcon.itemUIleft + \
                 SmallIcon.left + \
                 self.leftIndex * SmallIcon.width + \
                 (self.weightX * SmallIcon.width - SmallIcon.diffW) // 2
        self.y = SmallIcon.itemUItop - \
                 (SmallIcon.top +
                  self.topIndex * SmallIcon.height +
                  (self.weightY * SmallIcon.height - SmallIcon.diffH) // 2)
        self.weightList = weightList
        self.weightMapList = weightMapList
    def update(self):
        pass

    def draw(self):
        self.image.draw(self.x, self.y)


class Button:
    Non = 'UI\\buttonNon.png'
    On = 'UI\\buttonOn.png'
    left = 450
    top = 1000
    width = 75
    imageW = 54
    imageH = 51

    def __init__(self, buttonN):
        self.imageNon = load_image(Button.Non)
        self.imageOn = load_image(Button.On)
        self.x = Button.left + Button.width * buttonN + Button.imageW // 2
        self.y = gamePlay.HEIGHT - (Button.top + Button.imageH // 2)
        if buttonN == marketFramework.button:
            self.MouseOn = True
        else:
            self.MouseOn = False
        self.buttonN = buttonN

    def update(self):
        pass

    def draw(self):
        if self.MouseOn:
            self.imageOn.draw(self.x, self.y)
        else:
            self.imageNon.draw(self.x, self.y)

    def mouseOn(self, x, y, button):
        if button == self.buttonN:
            self.MouseOn = True
            return False
        if self.x - Button.imageW / 2 < x < self.x + Button.imageW / 2 and \
                self.y - Button.imageH / 2 < y < self.y + Button.imageH / 2:
            self.MouseOn = True
            return True
        else:
            self.MouseOn = False
            return False

    def mouseOff(self):
        self.MouseOn = False
    def returnButton(self):
        return self.buttonN
