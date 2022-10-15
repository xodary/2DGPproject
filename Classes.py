import Map
import random
import game_framework
from pico2d import *

WIDTH, HEIGHT = 1200, 822


mapping = [['shot', 'shot', 'blood', 'blood', 'milk', 'milk', 'cup', 'cup', 'cup', 'cup', 1, 1, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 2, 2],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
           [0, 0, 'trash', 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

menuQueue = []

running = True
class Pinn:
    stopMoving = True
    frame = 0
    x = WIDTH // 2 - 100
    y = HEIGHT // 2
    oldX = x
    oldY = y
    dirX = 0
    dirY = 0
    line = 0
    stop = 0
    item = None
    coffee = None
    blood = None

    def __init__(self):
        self.character = load_image('character\\pinn.png')
        self.coffee = load_image('order\\bubble\\bean.png')
        self.blood = load_image('order\\bubble\\blood.png')
        self.milk = load_image('order\\bubble\\milkbubble.png')
    def handle_events(self):
        events = get_events()
        for event in events:
            if event.type == SDL_QUIT or event.key == SDLK_ESCAPE:
                game_framework.quit()
            elif event.type == SDL_KEYDOWN:
                self.stopMoving = False
                if event.key == SDLK_RIGHT:
                    self.dirX += 1
                elif event.key == SDLK_LEFT:
                    self.dirX -= 1
                elif event.key == SDLK_UP:
                    self.dirY += 1
                elif event.key == SDLK_DOWN:
                    self.dirY -= 1
                elif event.key == SDLK_ESCAPE:
                    game_framework.quit()
                elif event.key == SDLK_SPACE:
                    if type(mapping[int(HEIGHT - self.y - 328) // 35 - 1][int(self.x - 264) // 35]) == Zombie and \
                            mapping[int(HEIGHT - self.y - 328) // 35 - 1][int(self.x - 264) // 35].state == 'ready' and\
                            self.stop == 4:
                        global menuQueue
                        menuQueue.append(mapping[int(HEIGHT - self.y - 328) // 35 - 1][int(self.x - 264) // 35].menu)
                        mapping[int(HEIGHT - self.y - 328) // 35 - 1][int(self.x - 264) // 35].state = 'wait'
                    elif mapping[int(HEIGHT - self.y - 328) // 35 - 1][int(self.x - 264) // 35] == 'shot' and self.stop == 4:
                        self.item = 'shot'
                    elif mapping[int(HEIGHT - self.y - 328) // 35 - 1][int(self.x - 264) // 35] == 'blood' and self.stop == 4:
                        self.item = 'blood'
                    elif mapping[int(HEIGHT - self.y - 328) // 35 - 1][int(self.x - 264) // 35] == 'milk' and self.stop == 4:
                        self.item = 'milk'
                    elif (mapping[int(HEIGHT - self.y - 328) // 35 - 1][int(self.x - 264) // 35] == 'trash' and\
                         self.item != None and self.stop == 4) or\
                        (mapping[int(HEIGHT - self.y - 328) // 35 + 1][int(self.x - 264) // 35] == 'trash' and\
                         self.item != None and self.stop == 0) or\
                        (mapping[int(HEIGHT - self.y - 328) // 35][int(self.x - 264) // 35 + 1] == 'trash' and\
                         self.item != None and self.stop == 2) or\
                        (mapping[int(HEIGHT - self.y - 328) // 35 + 1][int(self.x - 264) // 35 + 1] == 'trash' and\
                         self.item != None and self.stop == 1) or\
                        (mapping[int(HEIGHT - self.y - 328) // 35 - 1][int(self.x - 264) // 35 + 1] == 'trash' and\
                         self.item != None and self.stop == 3):
                        self.item = None

            elif event.type == SDL_KEYUP:
                if event.key == SDLK_RIGHT:
                    self.dirX -= 1
                elif event.key == SDLK_LEFT:
                    self.dirX += 1
                elif event.key == SDLK_UP:
                    self.dirY -= 1
                elif event.key == SDLK_DOWN:
                    self.dirY += 1

    def LineSet(self):
        if self.dirX > 0 and self.dirY > 0:
            self.line = 8
            self.stop = 3
        elif self.dirX < 0 and self.dirY > 0:
            self.line = 7
            self.stop = 5
        elif self.dirX < 0 and self.dirY < 0:
            self.line = 2
            self.stop = 7
        elif self.dirX > 0 and self.dirY < 0:
            self.line = 3
            self.stop = 1
        else:
            if self.dirY > 0:
                self.line = 6
                self.stop = 4
            elif self.dirY < 0:
                self.line = 1
                self.stop = 0
            elif self.dirX > 0:
                self.line = 5
                self.stop = 2
            elif self.dirX < 0:
                self.line = 4
                self.stop = 6
            else:
                self.line = 0
                self.frame = 0
                self.stopMoving = True

    def draw(self):
        if self.stopMoving:
            self.character.clip_draw(self.stop * 92, (1260 - 140 * (self.line + 1)), 92, 140, self.x,
                                     self.y + 70 - 30)
        elif not self.stopMoving:
            self.character.clip_draw(self.frame * 92, (1260 - 140 * (self.line + 1)), 92, 140, self.x,
                                     self.y + 70 - 30)
            self.frame = (self.frame + 1) % 6
        if self.item != None:
            match self.item:
                case 'shot':
                    self.coffee.draw(self.x, self.y + 130)
                case 'blood':
                    self.blood.draw(self.x, self.y + 130)
                case 'milk':
                    self.milk.draw(self.x, self.y + 130)

        # 입체감
        if self.y > HEIGHT - 431 - 72:
            global kitchenTable
            kitchenTable.draw(366 + 257 // 2 + 1, HEIGHT - 431 - 72 // 2)
        if self.y > HEIGHT - 536 - 65:
            global table
            table.draw(688 + 63 // 2 + 1, HEIGHT - 536 - 65 // 2 - 1)
        if self.y > HEIGHT - 483 - 90:
            global chair
            chair.draw(759 + 60 // 2, HEIGHT - 483 - 90 // 2)
        if self.y > HEIGHT - 453 - 50:
            global trash
            trash.draw(334 + 30 // 2, HEIGHT - 453 - 50 // 2)

    def logic(self):
        # 대각선 이동
        if self.dirX * self.dirY != 0:
            self.x += self.dirX * 15 * (1 / math.sqrt(2))
            self.y += self.dirY * 15 * (1 / math.sqrt(2))
        else:
            self.x += self.dirX * 15
            self.y += self.dirY * 15
        if (self.x - 264 - 92 // 4) // 35 < 0 or (
            self.x - 264 + 92 // 4) // 35 > 15 or (
            HEIGHT - self.y - 328) // 35 < 0 or (
            HEIGHT - self.y - 328) // 35 > 8 or (
                mapping[int(HEIGHT - self.y - 328) // 35][int(self.x - 264 - 92 // 4) // 35] != 0 or 
                mapping[int(HEIGHT - self.y - 328) // 35][int(self.x - 264 + 92 // 4) // 35] != 0):
            self.x = self.oldX
            self.y = self.oldY
        else:
            self.oldX = self.x
            self.oldY = self.y
        self.LineSet()


    def grabSomething(self):
        pass

# 수정 요망 (입구 좌표)
stageEntrance = [[562, HEIGHT - 626],
                 [],
                 [],
                 [],
                 []]

tables = [[[False, 0, HEIGHT - 530, 774, HEIGHT - 370, 1, 14], [False, 1]],
          [[False,],[False,],[False,]],
          [[False,],[False,],[False,],[False,]],
          [[False,],[False,],[False,],[False,],[False,]],
          [[False,],[False,],[False,],[False,],[False,],[False,]]]
stage = 0

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

    def __init__(self):
        # gender = random.randint(0, 2)
        # if gender == 0:
        self.image = load_image("character\\girlZombieSprite.png")
        self.BirthImage = load_image("character\\GirlZombiebirthSprite.png")
        self.bar = load_image("order\\bubble\\bar.png")
        self.gauge = load_image("order\\bubble\\gauge.png")
        self.readyOrder = load_image("order\\bubble\\ready.png")
        self.xPos = random.randint(100, 850)
        self.yPos = random.randint(100, 150)
        match random.randint(0, 2):
            case 0:
                self.menu = 'bloodAme'
            case 1:
                self.menu = 'Latte'
        # else:
        #     self.image = load_image("character\\boyZombieSprite.png")

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
        if self.waitingTime > 54:
            self.state = 'fail'
            mapping[self.index[0]][self.index[1]] = 0
            mapping[self.index[0]][self.index[1] + 1] = 0
            tables[stage][self.tableNum][0] = False
        pass

    def ThanksBye(self):
        pass

    def FailServe(self):
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
            case 'fail':
                self.FailServe()
                
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
                for width in range(0, 54 - self.waitingTime + 1):
                    self.gauge.draw(self.xPos - 60 // 2 + 3 + width, self.yPos + 120, 1, 8)
                self.image.clip_draw(105 * (self.frame // 8), 480 - 120 - 120 * 0, 105, 120, self.xPos, self.yPos + 40)
                self.frame = (self.frame + 1) % 16
            case _:
                self.image.clip_draw(105 * (self.frame // 4), 480 - 120 - 120 * self.line, 105, 120, self.xPos, self.yPos + 40)
                self.frame = (self.frame + 1) % 16
        if self.yPos > HEIGHT - 536 - 65:
            global table
            table.draw(688 + 63 // 2 + 1, HEIGHT - 536 - 65 // 2 - 1)
        if self.yPos > HEIGHT - 483 - 90:
            global chair
            chair.draw(759 + 60 // 2, HEIGHT - 483 - 90 // 2)



pinn = None
background = None
kitchenTable = None
table = None
wall = None
bubbleBean = None
bubbleBlood = None
zombies = [None]
chair = None
bubbleframe = 0
firstbubble = False
bloodAmericano = None
Latte = None
trash = None

def enter():
    global pinn, background, kitchenTable, table, wall, bubbleBean, bubbleBlood, chair
    pinn = Pinn()
    zombies[0] = Zombie()
    background = load_image('map\\map.png')
    kitchenTable = load_image("map\\kitchenTable.png")
    wall = load_image('map\\wall.png')
    table = load_image('map\\table.png')
    bubbleBean = load_image('order\\bubble\\coffeebubbleSprite.png')
    bubbleBlood = load_image('order\\bubble\\bloodbubbleSprite.png')
    chair = load_image('map\\chair.png')
    global bloodAmericano, Latte
    bloodAmericano = load_image('order\\bloodAmericano.png')
    Latte = load_image('order\\Latte.png')
    global trash
    trash = load_image('map\\trash.png')
    global bubblemilk
    bubblemilk = load_image('order\\bubble\\milkbubbleSprite.png')
def update():
    pinn.logic()
    for zombie in zombies:
        zombie.logic()
        if zombie.yPos < 0:
            del zombie

def handle_events():
    pinn.handle_events()

def draw():
    clear_canvas()
    background.draw(WIDTH // 2, HEIGHT // 2)
    for zombie in zombies:
        if pinn.y < zombie.yPos:
            zombie.draw()
    pinn.draw()
    wall.draw(230 + 626 // 2, HEIGHT - 253 - 424 // 2)
    for zombie in zombies:
        if pinn.y > zombie.yPos - 20:
            zombie.draw()

    global bubbleframe  # bubbleframe은 평소에 0임. 3을 바라보면 말풍선이 생긴다.
    if mapping[int(HEIGHT - pinn.y - 328) // 35 - 1][int(pinn.x - 264) // 35] == 'shot' and pinn.stop == 4:
        bubbleBean.clip_draw(50 * bubbleframe, 0, 50, 50, 273 + 50 // 2, HEIGHT - 183 - 50 // 2)
        if bubbleframe < 2:
            bubbleframe = bubbleframe + 1
    elif mapping[int(HEIGHT - pinn.y - 328) // 35 - 1][int(pinn.x - 264) // 35] == 'blood' and pinn.stop == 4:
        bubbleBlood.clip_draw(50 * bubbleframe, 0, 50, 50, 343 + 50 // 2, HEIGHT - 150 - 50 // 2)
        if bubbleframe < 2:
            bubbleframe = bubbleframe + 1
    elif mapping[int(HEIGHT - pinn.y - 328) // 35 - 1][int(pinn.x - 264) // 35] == 'milk' and pinn.stop == 4:
        bubblemilk.clip_draw(50 * bubbleframe, 0, 50, 50, 430 + 50 // 2, HEIGHT - 180 - 50 // 2)
        if bubbleframe < 2:
            bubbleframe = bubbleframe + 1
    else:
        bubbleframe = 0

    for index, menu in enumerate(menuQueue):
        match menu:
            case 'bloodAme':
                bloodAmericano.draw(100 + index * 173, HEIGHT - (226 // 2))
            case 'Latte':
                Latte.draw(100 + index * 173, HEIGHT - (226 // 2))
    
    update_canvas()
    delay(0.05)

def exit():
    global pinn
    del pinn

def test_self():
    import sys
    this_module = sys.modules['__main__']
    pico2d.open_canvas(WIDTH, HEIGHT)
    game_framework.run(this_module)
    pico2d.close_canvas()


if __name__ == '__main__':
    test_self()
