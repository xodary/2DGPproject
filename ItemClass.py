from pico2d import *
import gamePlay
import marketFramework
import pinnClass
import AllObjectClass

MAKEBIGICON, MAKESMALLICON, MAKEFURNITURE = range(3)
event_name = ['MAKEBIGICON', 'MAKESMALLICON', 'MAKEFURNITURE']


class ORDERBOX:
    def enter(self):
        self.image = load_image(self.orderBoxImage)
        self.x = self.orderLeft + self.orderWidth / 2
        self.y = gamePlay.HEIGHT - (self.orderTop + self.orderHeight / 2)
        self.MouseOn = False
        self.serverX, self.serverY = 0, 0

    def do(self):
        pass

    def exit(self):
        pass

    def mouseTest(self, x, y):
        if self.x - self.orderWidth / 2 < x < self.x + self.orderWidth / 2 and \
                self.y - self.orderHeight / 2 < y < self.y + self.orderHeight / 2:
            return True
        return False

    def makeBigIcon(self, x, y):
        icon = self
        icon.x, icon.y = x, y
        icon.add_event(MAKEBIGICON)
        AllObjectClass.add_object(icon, 6)
        return icon

    def draw(self):
        if self.MouseOn:
            self.image.draw(self.x, self.y)
        else:
            self.image.clip_draw(8, 8, self.orderWidth - 16, self.orderHeight - 16, self.x, self.y)


class BIGICON:
    width = 118
    height = 114
    imageW = 108
    imageH = 108
    left = 1041
    top = 270
    diffW = 10
    diffH = 6

    def enter(self):
        self.image = load_image(self.bigIconImage)
        self.fit = False

    def do(self):
        self.x, self.y = marketFramework.x, marketFramework.y

    def exit(self):
        pass

    def draw(self):
        if not self.fit:
            self.image.draw(self.x, self.y)
        else:
            # 수정
            self.image.draw(BIGICON.left + self.xIndex * BIGICON.width +
                            (self.weightX * BIGICON.width - BIGICON.diffW) // 2,
                            gamePlay.HEIGHT - (BIGICON.top + self.yIndex * BIGICON.height +
                                               (self.weightY * BIGICON.height - BIGICON.diffH) // 2))

    def mouseOffTest(self):
        xCenter = (self.x - BIGICON.left)
        yCenter = (gamePlay.HEIGHT - self.y - BIGICON.top)
        self.xIndex = int(xCenter - self.weightX / 2 * BIGICON.imageW) // BIGICON.imageW
        self.yIndex = int(yCenter - self.weightY / 2 * BIGICON.imageH) // BIGICON.imageH
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
        # myitem success 함수 설정
        for y in range(self.weightY):
            for x in range(self.weightX):
                if self.weightList[y][x] == 1:
                    pinnClass.Pinn.myitems[self.yIndex + y][self.xIndex + x].append(1)
        pinnClass.Pinn.myitems[self.yIndex][self.xIndex].append(self)
        self.fit = True


class SMALLICON:
    itemUIleft, itemUItop = 1920 - 176 * 4, 197 * 4
    left, top = 104, 160
    width, height = 84, 80
    imageW, imageH = 76, 76
    diffW = 8
    diffH = 4

    def enter(self):
        self.image = load_image(self.smallIconImage)

    def do(self):
        self.x, self.y = marketFramework.x, marketFramework.y

    def exit(self):
        pass

    def draw(self):
        if not self.fit:
            self.image.draw(self.x, self.y)
        else:
            self.image.draw(SMALLICON.itemUIleft + SMALLICON.left + self.xIndex * SMALLICON.width +
                            (self.weightX * SMALLICON.width - SMALLICON.diffW) // 2,
                            SMALLICON.itemUItop - (SMALLICON.top + self.yIndex * SMALLICON.height +
                                                   (self.weightY * SMALLICON.height - SMALLICON.diffH) // 2))

    def mouseOffTest(self):
        xCenter = (self.x - SMALLICON.left)
        yCenter = (gamePlay.HEIGHT - self.y - SMALLICON.top)
        self.xIndex = int(xCenter - self.weightX / 2 * SMALLICON.imageW) // SMALLICON.imageW
        self.yIndex = int(yCenter - self.weightY / 2 * SMALLICON.imageH) // SMALLICON.imageH
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
        # myitem success 함수 설정
        for y in range(self.weightY):
            for x in range(self.weightX):
                if self.weightList[y][x] == 1:
                    pinnClass.Pinn.myitems[self.yIndex + y][self.xIndex + x].append(1)
        pinnClass.Pinn.myitems[self.yIndex][self.xIndex].append(self)
        self.fit = True


class FURNITURE:
    def enter(self):
        pass

    def do(self):
        pass

    def exit(self):
        pass

    def draw(self):
        pass



next_state = {
    ORDERBOX: {MAKEBIGICON: BIGICON, MAKESMALLICON: SMALLICON, MAKEFURNITURE: FURNITURE},
    BIGICON: {MAKESMALLICON: SMALLICON, MAKEFURNITURE: FURNITURE},
    SMALLICON: {MAKEBIGICON: BIGICON, MAKEFURNITURE: FURNITURE},
    FURNITURE: {MAKEBIGICON: BIGICON, MAKESMALLICON: SMALLICON}
}


class Myitem:
    def __init__(self, orderBoxImage, bigIconImage, smallIconImage, furnitureImage,
                 orderLeft, orderTop, orderWidth, orderHeight,
                 weightX, weightY, weightMapX, weightMapY,
                 furnitureWidth, furnitureHeight, weightList=None, weightMapList=None, bubbleImage=None):

        # weightList 특별 처리
        if weightList:
            self.weightList = weightList
        else:
            self.weightList = [[1 for i in range(weightX)] for j in range(weightY)]
        if weightMapList:
            self.weightMapList = weightMapList
        else:
            self.weightMapList = [[1 for i in range(weightMapX)] for j in range(weightMapY)]
        self.orderBoxImage = orderBoxImage
        self.bigIconImage = bigIconImage
        self.smallIconImage = smallIconImage
        self.furnitureImage = furnitureImage
        self.bubbleImage = bubbleImage
        self.bubbleSize = 100
        self.orderLeft, self.orderTop = orderLeft, orderTop
        self.orderWidth, self.orderHeight = orderWidth, orderHeight
        self.weightX, self.weightY = weightX, weightY
        self.weightMapX, self.weightMapY = weightMapX, weightMapY
        self.furnitureWidth, self.furnitureHeight = furnitureWidth, furnitureHeight
        self.fit = False
        self.xIndex, self.yIndex = 0, 0

        self.MouseOn = False
        self.event_que = []
        self.cur_state = ORDERBOX
        self.cur_state.enter(self)

    def add_event(self, event):
        self.event_que.insert(0, event)

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

    def draw(self):
        self.cur_state.draw(self)


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
