import gamePlay
import zombieClass
from pico2d import *


class Recipe:
    def __init__(self, image, left, bottom, right, top, price, menuImage, priceone):
        self.image = load_image(image)
        self.left, self.bottom, self.right, self.top = left, bottom, right, top
        self.bgm = load_wav('sound\\coins.wav')
        self.menuImage = menuImage
        self.price = price
        self.priceOne = priceone
        self.MouseOn = False

    def update(self):
        pass

    def mouseTest(self, x, y):
        if self.left < x < self.right and self.bottom < y < self.top:
            return True
        return False

    def draw(self):
        if self.MouseOn:
            self.image.draw((self.right + self.left) // 2, (self.top + self.bottom) // 2)
        else:
            self.image.clip_draw(8, 8, self.right - self.left - 16, self.top - self.bottom - 16,
                                 (self.right + self.left) // 2, (self.top + self.bottom) // 2)
