from pico2d import *
import gamePlay

class marketSell:
    def __init__(self, pngName, miniItemImage, left, top, width, height, weightX, weightY):
        self.image = load_image(pngName)
        self.mini = load_image(miniItemImage)
        self.x = left + width / 2
        self.y = gamePlay.HEIGHT - (top + height / 2)
        self.width = width
        self.height = height
        self.weightX = weightX
        self.weightY = weightY
        self.MouseOn = False

    def update(self):
        pass

    def mouse(self):
        self.MouseOn = not self.MouseOn

    def draw(self):
        if self.MouseOn:
            self.image.draw(self.x, self.y)
        else:
            self.image.clip_draw(8, 8, self.width - 16, self.height - 16, self.x, self.y)


