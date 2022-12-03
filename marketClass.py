import game_framework
from pico2d import *
import gamePlay
import marketFramework
import pinnClass
import AllObjectClass
import marketMap


class MarketUI_Background:
    menuL, menuR, menuB, menuT = 189, 189 + 700, 1280 - (270 + 695), 1280 - 270
    itemL, itemR, itemB, itemT = 1041, 1041 + 707, 1280 - (270 + 678), 1280 - 270

    def __init__(self):
        self.image = load_image('UI\\marketUI.png')
        self.items = None
        self.buttons = None
        self.buttonNum = 0
        for item in pinnClass.Pinn.myitemList:
            item.add_event(MAKEBIGICON)
            item.fit = True
            AllObjectClass.add_object(item, 6)

    def update(self):
        pass

    def draw(self):
        self.image.draw(gamePlay.viewWIDTH // 2, gamePlay.viewHEIGHT // 2)

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
                return None
        # push items
        if MarketUI_Background.itemL <= x <= MarketUI_Background.itemR and \
                MarketUI_Background.itemB <= y <= MarketUI_Background.itemT:
            mx = (x - MarketUI_Background.itemL) // BIGICON.imageW
            my = (MarketUI_Background.itemT - y) // BIGICON.imageH
            item = pinnClass.Pinn.myitems[my][mx]
            if item:
                AllObjectClass.remove_object(item)
                AllObjectClass.add_object(item, 6)
                pinnClass.Pinn.myitemList.remove(item)
                # 팔기
                for y in range(item.weightY):
                    for x in range(item.weightX):
                        if item.weightList[y][x] == 1:
                            pinnClass.Pinn.myitems[item.yIndex + y][item.xIndex + x] = None
                return item
        # 사기
        elif MarketUI_Background.menuL <= x <= MarketUI_Background.menuR and \
                MarketUI_Background.menuB <= y <= MarketUI_Background.menuT:
            for menu in self.items[self.buttonNum]:
                if menu.cur_state.mouseTest(menu, x, y):
                    return menu.cur_state.makeBigIcon(menu, x, y)
        return None

    def MouseMotion(self, x, y, mouseOn):
        for Button in self.buttons:
            Button.mouseOn(x, y, self.buttonNum)
        if mouseOn:
            # item 쪽에 마우스 올리면 칸에 쏙 들어감
            if MarketUI_Background.itemL <= x <= MarketUI_Background.itemR and \
                    MarketUI_Background.itemB <= y <= MarketUI_Background.itemT:
                if mouseOn.cur_state.mouseOffTest(mouseOn):
                    mouseOn.fit = True
                else:
                    mouseOn.fit = False
            else:
                mouseOn.fit = False
        for item in self.items[self.buttonNum]:
            if item.cur_state.mouseTest(item, x, y):
                item.MouseOn = True
            else:
                item.MouseOn = False

    def MouseButtonUp(self, mouseOn):
        if mouseOn:
            if mouseOn.cur_state.mouseOffTest(mouseOn):
                mouseOn.cur_state.success(mouseOn)
                marketFramework.itemImages.append(mouseOn)
            else:
                AllObjectClass.remove_object(mouseOn)

    def exit(self):
        for item in self.items[self.buttonNum]:
            AllObjectClass.remove_object(item)

        for item in pinnClass.Pinn.myitemList:
            AllObjectClass.remove_object(item)


class Inventory:
    itemUIleft, itemUItop = 1920 - 176 * 4, 197 * 4
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
        self.tempXindex, self.tempYindex = 0, 0

    def update(self):
        pass

    def draw(self):
        self.image.clip_draw(0, 0, self.ImageW, self.ImageH, self.x, self.y, self.width, self.height)

    def MouseButtonDown(self, x, y):
        click = None
        if Inventory.itemUIleft <= x <= gamePlay.viewWIDTH and \
                0 <= y <= Inventory.itemUItop:
            mx = (x - Inventory.itemUIleft - SMALLICON.left) // SMALLICON.width
            my = (Inventory.itemUItop - SMALLICON.top - y) // SMALLICON.height
            click = pinnClass.Pinn.myitems[my][mx]
            if click:
                self.tempXindex, self.tempYindex = click.xIndex, click.yIndex
                self.bornSmall = True
                click.fit = False
                pinnClass.Pinn.myitemList.remove(click)
                for y in range(click.weightY):
                    for x in range(click.weightX):
                        if click.weightList[y][x] == 1:
                            pinnClass.Pinn.myitems[click.yIndex + y][click.xIndex + x] = None

        else:
            mx = (x + gamePlay.cameraLEFT - gamePlay.mapstartX) // gamePlay.boxSizeW
            my = (gamePlay.HEIGHT - y - gamePlay.cameraBOTTOM - gamePlay.mapstartY) // gamePlay.boxSizeH
            holding = gamePlay.mapping[my][mx]
            if isinstance(holding, Myitem):
                click = holding
                self.tempXindex, self.tempYindex = click.xMapIndex, click.yMapIndex
                self.bornSmall = False
                click.fit = False
                gamePlay.furnitureList.remove(click)
                for y in range(click.weightMapY):
                    for x in range(click.weightMapX):
                        if click.weightMapList[y][x] == 1:
                            gamePlay.mapping[click.yMapIndex + y][click.xMapIndex + x] = 0
        return click

    def MouseMotion(self, x, y, click):
        if click:
            if Inventory.itemUIleft < x < gamePlay.viewWIDTH and 0 < y < Inventory.itemUItop and gamePlay.pinn.inven:
                click.add_event(MAKESMALLICON)
                AllObjectClass.remove_object(click)
                AllObjectClass.add_object(click, 6)
                if click.cur_state.mouseOffTest(click):
                    click.fit = True
                else:
                    click.fit = False
            else:
                click.add_event(MAKEFURNITURE)
                AllObjectClass.remove_object(click)
                AllObjectClass.add_object(click, 1)
                if click.cur_state.mouseOffTest(click):
                    click.fit = True
                else:
                    click.fit = False

    def MouseButtonUp(self, click):
        if click:
            if click.cur_state.mouseOffTest(click):
                click.cur_state.success(click)
            else:
                click.fit = True
                if self.bornSmall:
                    click.add_event(MAKESMALLICON)
                    AllObjectClass.remove_object(click)
                    AllObjectClass.add_object(click, 6)
                    pinnClass.Pinn.myitemList.append(click)
                    click.xIndex, click.yIndex = self.tempXindex, self.tempYindex
                    for y in range(click.weightY):
                        for x in range(click.weightX):
                            if click.weightList[y][x] == 1:
                                pinnClass.Pinn.myitems[click.yIndex + y][click.xIndex + x] = click
                else:
                    click.add_event(MAKEFURNITURE)
                    AllObjectClass.remove_object(click)
                    AllObjectClass.add_object(click, 1)
                    gamePlay.furnitureList.append(click)
                    click.xMapIndex, click.yMapIndex = self.tempXindex, self.tempYindex
                    for y in range(click.weightMapY):
                        for x in range(click.weightMapX):
                            if click.weightMapList[y][x] == 1:
                                gamePlay.mapping[click.yMapIndex + y][click.xMapIndex + x] = click


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
        # import copy
        # icon = copy.deepcopy(self)
        icon = Myitem(self.orderBoxImage, self.bigIconImage, self.smallIconImage, self.furnitureImage,
                      self.orderLeft, self.orderTop, self.orderWidth, self.orderHeight,
                      self.weightX, self.weightY, self.weightMapX, self.weightMapY,
                      self.furnitureWidth, self.furnitureHeight, self.weightList, self.weightMapList, self.bubbleImage)
        icon.add_event(MAKEBIGICON)
        icon.x, icon.y = x, y
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
                        if pinnClass.Pinn.myitems[self.yIndex + y][self.xIndex + x]:
                            return False
        else:
            return False
        return True

    def success(self):
        # myitem success 함수 설정
        for y in range(self.weightY):
            for x in range(self.weightX):
                if self.weightList[y][x] == 1:
                    pinnClass.Pinn.myitems[self.yIndex + y][self.xIndex + x] = self
        pinnClass.Pinn.myitemList.append(self)
        self.fit = True


class SMALLICON:
    left, top = 104, 160
    width, height = 84, 80
    imageW, imageH = 76, 76
    diffW = 8
    diffH = 4

    def enter(self):
        self.image = load_image(self.smallIconImage)

    def do(self):
        if gamePlay.MAINMAP:
            self.x, self.y = gamePlay.x, gamePlay.y
        else:
            self.x, self.y = marketMap.x, marketMap.y

    def exit(self):
        pass

    def draw(self):
        if not self.fit:
            self.image.draw(self.x, self.y)
        else:
            self.image.draw(Inventory.itemUIleft + SMALLICON.left + self.xIndex * SMALLICON.width +
                            (self.weightX * SMALLICON.width - SMALLICON.diffW) // 2,
                            Inventory.itemUItop - (SMALLICON.top + self.yIndex * SMALLICON.height +
                                                   (self.weightY * SMALLICON.height - SMALLICON.diffH) // 2))

    def mouseOffTest(self):
        xCenter = self.x - Inventory.itemUIleft - SMALLICON.left
        yCenter = Inventory.itemUItop - SMALLICON.top - self.y
        self.xIndex = int(xCenter - self.weightX / 2 * SMALLICON.imageW) // SMALLICON.imageW
        self.yIndex = int(yCenter - self.weightY / 2 * SMALLICON.imageH) // SMALLICON.imageH
        print(self.xIndex, self.yIndex)
        if 0 <= self.xIndex <= 5 and 0 <= self.yIndex <= 5 and \
                0 <= self.xIndex + self.weightX - 1 <= 5 and 0 <= self.yIndex + self.weightY - 1 <= 5:
            for y in range(self.weightY):
                for x in range(self.weightX):
                    if self.weightList[y][x] == 1:
                        if pinnClass.Pinn.myitems[self.yIndex + y][self.xIndex + x]:
                            return False
        else:
            return False
        return True

    def success(self):
        # myitem success 함수 설정
        for y in range(self.weightY):
            for x in range(self.weightX):
                if self.weightList[y][x] == 1:
                    pinnClass.Pinn.myitems[self.yIndex + y][self.xIndex + x] = self
        pinnClass.Pinn.myitemList.append(self)
        self.fit = True


class FURNITURE:

    def enter(self):
        self.image = load_image(self.furnitureImage)

    def do(self):
        if gamePlay.MAINMAP:
            self.x, self.y = gamePlay.x, gamePlay.y
        else:
            self.x, self.y = marketMap.x, marketMap.y
        if not self.fit:
            self.down = self.y - self.furnitureHeight / 2
        else:
            self.down = gamePlay.HEIGHT - (gamePlay.mapstartY + self.yMapIndex * gamePlay.boxSizeH +
                                           self.weightMapY * gamePlay.boxSizeH)

    def exit(self):
        pass

    def draw(self):
        if not self.fit:
            self.image.draw(self.x, self.y)
        else:
            self.image.draw(gamePlay.mapstartX + gamePlay.boxSizeW * self.xMapIndex +
                            self.weightMapX * gamePlay.boxSizeW / 2 - gamePlay.cameraLEFT,
                            gamePlay.HEIGHT - (
                                    gamePlay.mapstartY +
                                    gamePlay.boxSizeH * self.yMapIndex + gamePlay.boxSizeH * self.weightMapY -
                                    self.furnitureHeight / 2) - gamePlay.cameraBOTTOM)

    def __lt__(self, otherObj):
        return self.image < otherObj.image

    def makeBubble(self):
        if self.bubbleImage != None:
            return (gamePlay.mapstartX + gamePlay.boxSizeW * self.xMapIndex +
                    self.weightMapX * gamePlay.boxSizeW / 2,
                    gamePlay.HEIGHT - (
                            gamePlay.mapstartY +
                            gamePlay.boxSizeH * self.yMapIndex + gamePlay.boxSizeH * self.weightMapY -
                            self.furnitureHeight / 2) + 150,
                    self.bubbleImage, self.bubbleSize)

    def bubbleTest(self):
        if self.bubbleImage:
            return True
        else:
            return False

    def mouseOffTest(self):
        xCenter = self.x + gamePlay.cameraLEFT - gamePlay.mapstartX
        yCenter = gamePlay.HEIGHT - (self.y + gamePlay.cameraBOTTOM) - gamePlay.mapstartY
        self.xMapIndex = int(xCenter - self.weightMapX * gamePlay.boxSizeW / 2) // gamePlay.boxSizeW
        self.yMapIndex = int(
            yCenter + self.furnitureHeight / 2 - self.weightMapY * gamePlay.boxSizeH / 2) // gamePlay.boxSizeH
        print(self.xMapIndex, self.yMapIndex)
        if 0 <= self.xMapIndex - gamePlay.MainMapPlusX and \
                self.xMapIndex - gamePlay.MainMapPlusX + self.weightMapX - 1 < 32 and \
                0 <= self.yMapIndex - gamePlay.MainMapPlusY and \
                0 <= self.yMapIndex - gamePlay.MainMapPlusY + self.weightMapY - 1 < 9 and gamePlay.MAINMAP:
            for y in range(self.weightMapY):
                for x in range(self.weightMapX):
                    if self.weightMapList[y][x] == 1:
                        if gamePlay.mapping[self.yMapIndex + y][self.xMapIndex + x] != 0:
                            return False
        else:
            return False
        return True

    def success(self):
        # myitem success 함수 설정
        for y in range(self.weightMapY):
            for x in range(self.weightMapX):
                if self.weightMapList[y][x] == 1:
                    gamePlay.mapping[self.yMapIndex + y][self.xMapIndex + x] = self
        gamePlay.furnitureList.append(self)
        self.fit = True
        self.woodyHit.play()
        self.down = gamePlay.mapstartX + gamePlay.MainMapPlusX * gamePlay.boxSizeW + \
                    self.yMapIndex * gamePlay.boxSizeH + self.weightMapY * gamePlay.boxSizeH / 2


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
        self.MouseOn = False
        self.event_que = []
        self.cur_state = ORDERBOX
        self.cur_state.enter(self)
        self.down = 0
        self.woodyHit = load_wav('sound\\woodyHit.wav')

    def __getstate__(self):
        state = {'xIndex': self.xIndex, 'yIndex': self.yIndex,
                 'xMapIndex': self.xMapIndex, 'yMapIndex': self.yMapIndex,
                 'fit': self.fit, 'cur_state': self.cur_state}
        return state

    # 복구할 때
    def __setstate__(self, state):
        self.__init__()  # 강제로 생성자를 호출해서, 일단은 전체
        # 속성을 다 확보한다
        # 업데이트를 통해서, 속성값을 복구한 값으로 변경한다.
        self.__dict__.update(state)

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
            self.cur_state.enter(self)

    def draw(self):
        self.cur_state.draw(self)


class Table(Myitem):
    def __init__(self, orderBoxImage, bigIconImage, smallIconImage, furnitureImage,
                 orderLeft, orderTop, orderWidth, orderHeight,
                 weightX, weightY, weightMapX, weightMapY,
                 furnitureWidth, furnitureHeight, weightList=None, weightMapList=None, bubbleImage=None):
        super().__init__(orderBoxImage, bigIconImage, smallIconImage, furnitureImage,
                         orderLeft, orderTop, orderWidth, orderHeight,
                         weightX, weightY, weightMapX, weightMapY,
                         furnitureWidth, furnitureHeight, weightList, weightMapList, bubbleImage)
        self.sit = False
        self.sittingZombie = None


class waitingForSecond(Myitem):
    def __init__(self, orderBoxImage, bigIconImage, smallIconImage, furnitureImage,
                 orderLeft, orderTop, orderWidth, orderHeight,
                 weightX, weightY, weightMapX, weightMapY,
                 furnitureWidth, furnitureHeight, bgm=None, weightList=None, weightMapList=None, bubbleImage=None):
        super().__init__(orderBoxImage, bigIconImage, smallIconImage, furnitureImage,
                         orderLeft, orderTop, orderWidth, orderHeight,
                         weightX, weightY, weightMapX, weightMapY,
                         furnitureWidth, furnitureHeight, weightList, weightMapList, bubbleImage)

        self.waitingTime = 3
        self.bubbleload = load_image(self.bubbleImage)
        self.ready = False
        self.wait = False
        self.bgm = load_wav(bgm)
        self.bgm.set_volume(32)

    def click(self):
        self.bgm.play()
        self.wait = True

    def waiting(self):
        self.waitingTime -= game_framework.frame_time
        if self.waitingTime <= 0:
            self.waitingTime = 3
            self.ready = True
            self.wait = False

    def update(self):
        super().update()
        if self.wait:
            self.waiting()

    def draw(self):
        super().draw()
        if self.ready:
            self.bubbleload.clip_draw(0, 0, 100, 100, gamePlay.mapstartX + gamePlay.boxSizeW * self.xMapIndex +
                                 self.weightMapX * gamePlay.boxSizeW / 2 - gamePlay.cameraLEFT,
                                 gamePlay.HEIGHT - (
                                         gamePlay.mapstartY +
                                         gamePlay.boxSizeH * self.yMapIndex + gamePlay.boxSizeH * self.weightMapY -
                                         self.furnitureHeight / 2) + 150 - gamePlay.cameraBOTTOM)

class noWait(Myitem):
    def __init__(self, orderBoxImage, bigIconImage, smallIconImage, furnitureImage,
                 orderLeft, orderTop, orderWidth, orderHeight,
                 weightX, weightY, weightMapX, weightMapY,
                 furnitureWidth, furnitureHeight, bgm, weightList=None, weightMapList=None, bubbleImage=None):
        super().__init__(orderBoxImage, bigIconImage, smallIconImage, furnitureImage,
                         orderLeft, orderTop, orderWidth, orderHeight,
                         weightX, weightY, weightMapX, weightMapY,
                         furnitureWidth, furnitureHeight, weightList, weightMapList, bubbleImage)

        self.bubbleload = load_image(self.bubbleImage)
        self.bgm = load_wav(bgm)
        self.bgm.set_volume(32)

    def click(self):
        self.bgm.play()
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
