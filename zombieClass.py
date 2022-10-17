from std import *

class Zombie:

    frame = 0
    line = 0
    birthingTime = 0
    xPos = 0
    yPos = 0
    xDir = 0
    yDir = 0
    tableNum = 0
    state = 'birth'
    index = [0, 0]
    waitingTime = 0
    menu = None
    bubbleCount = 0
    bubbleCountArray = [0, 1, 2, 1, 0]
    bubbleFrame = 0

    def __init__(self):
        self.gender = random.randint(0, 1)
        if self.gender == 0:
            self.image = load_image("character\\girlZombieSprite.png")
            self.BirthImage = load_image("character\\GirlZombiebirthSprite.png")
        else:
            self.image = load_image("character\\boySprite.png")
            self.BirthImage = load_image("character\\boyBirthSprite.png")
        self.bar = load_image("order\\bubble\\bar.png")
        self.gauge = load_image("order\\bubble\\gauge.png")
        self.readyOrder = load_image("order\\bubble\\ready.png")
        self.heart = load_image("order\\bubble\\heart.png")
        self.No = load_image("order\\bubble\\No.png")
        self.xPos = random.randint(100, 850)
        self.yPos = random.randint(80, 130)
        match random.randint(0, 1):
            case 0:
                self.menu = 'bloodAme'
            case 1:
                self.menu = 'Latte'


    def zombieBirth(self):
        self.frame = (self.birthingTime // 5) % 4
        self.line = self.birthingTime // 20
        self.BirthImage.clip_draw(105 * self.frame, 420 - 130 - 130 * self.line, 105, 130, self.xPos, self.yPos + 40)
        self.birthingTime = self.birthingTime + 1
        if self.birthingTime >= 60:
            self.state = 'walk'
            self.line = 0
            self.frame = 0

    def walkToCafe(self):
        global stage

        if self.yPos > stageEntrance[stage][1]:
            self.state = 'check'
            self.frame = 0
            return
        if self.xPos < stageEntrance[stage][0] - 20:
            self.xDir = 1
            self.yDir = 0
        elif self.xPos > stageEntrance[stage][0] + 20:
            self.xDir = -1
            self.yDir = 0
        elif self.yPos < stageEntrance[stage][1]:
            self.xDir = 0
            self.yDir = 1
        


    def checkTable(self):
        global tables
        for table in tables[stage]:
            if not table[0]:
                table[0] = True
                self.tableNum = table[1]
                self.state = 'walkTable'
                self.index[0] = table[5]
                self.index[1] = table[6]
                break
        if self.state != 'walkTable':
            self.state = 'bye'

    def walkToTable(self):
        global tables
        if self.yPos < tables[stage][self.tableNum][2]:
            self.yDir = 1
        elif self.xPos < tables[stage][self.tableNum][3]:
            self.yDir = 0
            self.xDir = 1
        elif self.yPos < tables[stage][self.tableNum][4]:
            self.xDir = 0
            self.yDir = 1
        else:
            self.xDir = 0
            self.yDir = 0
            self.state = 'ready'
            mapping[self.index[0]][self.index[1]] = self
            mapping[self.index[0]][self.index[1] + 1] = self

    def LineSet(self):
        if self.xDir > 0:
            self.line = 3
        elif self.xDir < 0:
            self.line = 2
        elif self.yDir > 0:
            self.line = 1
        else:
            self.line = 0


    def waitingOrder(self):
        self.waitingTime += 1
        if self.waitingTime > 54 * 10:
            self.state = 'bye'
            menuQueue.pop(0)
            mapping[self.index[0]][self.index[1]] = 0
            mapping[self.index[0]][self.index[1] + 1] = 0
            tables[stage][self.tableNum][0] = False


    def DrinkCoffee(self, result):
        if result == 'success':
            self.state = 'thanks'
        else:
            self.state = 'No'
        menuQueue.pop(0)

    def Thanks(self):
        if self.bubbleCount < 5 * 8 - 1:
            self.bubbleCount += 1
        else:
            self.state = 'bye'
            global tables
            tables[stage][self.tableNum][0] = False
        self.bubbleFrame = self.bubbleCountArray[self.bubbleCount // 8]

    def No(self):
        if self.bubbleCount < 5 * 8 - 1:
            self.bubbleCount += 1
        else:
            self.state = 'bye'
            global tables
            tables[stage][self.tableNum][0] = False
        self.bubbleFrame = self.bubbleCountArray[self.bubbleCount // 8]

    def bye(self):
        global tables
        if self.yPos > tables[stage][self.tableNum][2]:
            self.yDir = -1
        elif self.xPos > stageEntrance[stage][0]:
            self.yDir = 0
            self.xDir = -1
        else:
            self.xDir = 0
            self.yDir = -1


    def logic(self):
        match self.state:
            case 'walk':
                self.walkToCafe()
            case 'check':
                self.checkTable()
            case 'walkTable':
                self.walkToTable()
            case 'wait':
                self.waitingOrder()
            case 'thanks':
                self.Thanks()
            case 'No':
                self.Thanks()
            case 'bye':
                self.bye()
                
        self.LineSet()

        self.xPos += 6 * self.xDir 
        self.yPos += 6 * self.yDir 


    def draw(self):
        match self.state:
            case 'birth':
                self.zombieBirth()
            case 'ready':
                self.readyOrder.draw(self.xPos, self.yPos + 120)
                self.image.clip_draw(105 * (self.frame // 8), 480 - 120 - 120 * 0, 105, 120, self.xPos, self.yPos + 40)
                self.frame = (self.frame + 1) % 16
            case 'wait':
                self.bar.draw(self.xPos, self.yPos + 120)
                for width in range(0, 54 - (self.waitingTime // 10) + 1):
                    self.gauge.draw(self.xPos - 60 // 2 + 3 + width, self.yPos + 120, 1, 8)
                self.image.clip_draw(105 * (self.frame // 8), 480 - 120 - 120 * 0, 105, 120, self.xPos, self.yPos + 40)
                self.frame = (self.frame + 1) % 16
            case 'thanks':
                self.heart.clip_draw(self.bubbleFrame * 50, 0, 50, 50, self.xPos, self.yPos + 120)
                self.image.clip_draw(105 * (self.frame // 8), 480 - 120 - 120 * 0, 105, 120, self.xPos, self.yPos + 40)
                self.frame = (self.frame + 1) % 16
            case 'No':
                self.No.clip_draw(self.bubbleFrame * 50, 0, 50, 50, self.xPos, self.yPos + 120)
                self.image.clip_draw(105 * (self.frame // 8), 480 - 120 - 120 * 0, 105, 120, self.xPos, self.yPos + 40)
                self.frame = (self.frame + 1) % 16
            case _:
                self.image.clip_draw(105 * (self.frame // 4), 480 - 120 - 120 * self.line, 105, 120, self.xPos, self.yPos + 40)
                self.frame = (self.frame + 1) % 16
