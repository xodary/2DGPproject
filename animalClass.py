import marketClass
from pico2d import *
import BehaviorTree
import game_framework

class Cow(marketClass.Myitem):
    def __init__(self, orderBoxImage, bigIconImage, smallIconImage, furnitureImage,
                 orderLeft, orderTop, orderWidth, orderHeight,
                 weightX, weightY, weightMapX, weightMapY,
                 furnitureWidth, furnitureHeight, bgm=None, weightList=None, weightMapList=None, bubbleImage=None):
        super().__init__(orderBoxImage, bigIconImage, smallIconImage, furnitureImage,
                 orderLeft, orderTop, orderWidth, orderHeight,
                 weightX, weightY, weightMapX, weightMapY,
                 furnitureWidth, furnitureHeight, bgm, weightList, weightMapList, bubbleImage)
        self.frame = 0
        self.dirX, self.dirY = 0, 0
        self.xPos, self.yPos = 0, 0
        self.bt = None
        self.speed = 0





class Chicken(marketClass.Myitem):
    def __init__(self, orderBoxImage, bigIconImage, smallIconImage, furnitureImage,
                 orderLeft, orderTop, orderWidth, orderHeight,
                 weightX, weightY, weightMapX, weightMapY,
                 furnitureWidth, furnitureHeight, bgm=None, weightList=None, weightMapList=None, bubbleImage=None):
        super().__init__(orderBoxImage, bigIconImage, smallIconImage, furnitureImage,
                 orderLeft, orderTop, orderWidth, orderHeight,
                 weightX, weightY, weightMapX, weightMapY,
                 furnitureWidth, furnitureHeight, bgm, weightList, weightMapList, bubbleImage)
        if orderBoxImage =