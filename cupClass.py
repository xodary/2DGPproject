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

    def putItem(self, item):
        if item not in self.setting:
            self.setting.append(item.imageName)

    def checkCup(self, menu):
        if len(self.setting) != len(recipe[menu.imageName]):
            return False
        for element in recipe[menu.imageName]:
            if not element in self.setting:
                return False
        return True

    def draw(self):
        xPos = gamePlay.mapstartX + gamePlay.boxSizeW * self.xIndex + 36 // 2
        yPos = gamePlay.HEIGHT - gamePlay.mapstartY - gamePlay.boxSizeH * (self.yIndex - 1) - 34 // 2
        self.image.draw(xPos, yPos)
        for element in self.setting:
            self.settingImage = load_image(element)
            self.settingImage.draw(xPos, yPos + 50 + self.setting.index(element) * 60)
