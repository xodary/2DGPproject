from pico2d import *
import gamePlay

recipe = {'order\\bloodAmericano.png': ['bubble\\blood.png', 'bubble\\coffee.png'],
          'order\\eggLatte.png': ['bubble\\egg.png', 'bubble\\milk.png'],
          'order\\finger.png': ['bubble\\milk.png', 'bubble\\blood.png', 'bubble\\finger.png'],
          'order\\Latte.png': ['bubble\\milk.png', 'bubble\\coffee.png']}


class Cup:
    cupimage = "map1.6\\justCup.png"

    def __init__(self):
        self.setting = []
        self.settingImage = None
        self.xIndex = 0
        self.yIndex = 0
        self.image = load_image(Cup.cupimage)
        self.down = 0

    def putItem(self, item):
        if item not in self.setting:
            self.setting.append(item)

    def checkCup(self, menu):
        if len(self.setting) != len(recipe[menu]):
            return False
        for element in recipe[menu]:
            if not element in self.setting:
                return False
        return True

    def __lt__(self, otherObj):
        return self.image < otherObj.image

    def update(self):
        self.xPos = gamePlay.mapstartX + gamePlay.boxSizeW * self.xIndex
        self.yPos = gamePlay.HEIGHT - gamePlay.mapstartY - gamePlay.boxSizeH * self.yIndex
        # self.down = self.yPos - 70

    def draw(self):
        self.image.draw(self.xPos - gamePlay.cameraLEFT, self.yPos + 50 - gamePlay.cameraBOTTOM)
        for element in self.setting:
            self.settingImage = load_image(element)
            self.settingImage.clip_draw(0, 0, 100, 100,
                                        self.xPos - gamePlay.cameraLEFT,
                                        self.yPos + 100 + self.setting.index(element) * 60 - gamePlay.cameraBOTTOM,
                                        60, 60)
