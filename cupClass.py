from std import *


class Cup:
    def __init__(self):
        self.setting = []
        self.xIndex = 0
        self.yIndex = 0
        self.image = load_image("map\\justCup.png")
        self.coffee = load_image('order\\bubble\\bean.png')
        self.blood = load_image('order\\bubble\\blood.png')
        self.milk = load_image('order\\bubble\\milkbubble.png')

    def putItem(self, item):
        if item not in self.setting:
            self.setting.append(item)

    def checkCup(self, menu):
        match menu:
            case 'bloodAme':
                if 'shot' in self.setting and 'blood' in self.setting and len(self.setting) == 2:
                    return GOOD
            case 'Latte':
                if 'milk' in self.setting and 'shot' in self.setting and len(self.setting) == 2:
                    return GOOD
        return BAD

    def draw(self):
        xPos = mapstart[stage][0] + boxSizeW * self.xIndex + 36 // 2
        yPos = HEIGHT - mapstart[stage][1] - boxSizeH * (self.yIndex - 1) - 34 // 2
        self.image.draw(xPos, yPos)
        if 'shot' in self.setting:
            self.coffee.draw(xPos, yPos + 50 + self.setting.index('shot') * 60)
        if 'blood' in self.setting:
            self.blood.draw(xPos, yPos + 50 + self.setting.index('blood') * 60)
        if 'milk' in self.setting:
            self.milk.draw(xPos, yPos + 50 + self.setting.index('milk') * 60)
