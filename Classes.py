import Map
import random
import game_framework
from pico2d import *

WIDTH, HEIGHT = 1200, 822


mapping = [[3, 3, 4, 4, 5, 5, 5, 5, 5, 5, 1, 1, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 2, 2],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 6, 6, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
           [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 6, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]


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

    def __init__(self):
        self.character = load_image('character\\pinn.png')

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

            elif event.type == SDL_KEYUP:
                if event.key == SDLK_RIGHT:
                    self.dirX -= 1
                elif event.key == SDLK_LEFT:
                    self.dirX += 1
                elif event.key == SDLK_UP:
                    self.dirY -= 1
                elif event.key == SDLK_DOWN:
                    self.dirY += 1

    def draw(self):
        if self.stopMoving:
            self.character.clip_draw(self.stop * 92, (1260 - 140 * (self.line + 1)), 92, 140, self.x,
                                     self.y + 70 - 30)
        elif not self.stopMoving:
            self.character.clip_draw(self.frame * 92, (1260 - 140 * (self.line + 1)), 92, 140, self.x,
                                     self.y + 70 - 30)
            self.frame = (self.frame + 1) % 6

        global bubbleBean, bubbleBlood
        if mapping[int(HEIGHT - self.y - 328) // 35 - 1][int(self.x - 264) // 35] == 3 and self.stop == 4:
            bubbleBean.draw(273 + 50 // 2, HEIGHT - 183 - 50 // 2)
        if mapping[int(HEIGHT - self.y - 328) // 35 - 1][int(self.x - 264) // 35] == 4 and self.stop == 4:
            bubbleBlood.draw(344 + 50 // 2, HEIGHT - 150 - 50 // 2)

        # 입체감을 위해서
        global kitchenTableAlways, table
        if self.y > HEIGHT - 431 - 72:
            global kitchenTable
            kitchenTable.draw(366 + 257 // 2 + 1, HEIGHT - 431 - 72 // 2)
        if self.y > HEIGHT - 536 - 65:
            global table
            table.draw(688 + 63 // 2 + 1,
                              HEIGHT - 536 - 65 // 2 - 1)

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


    def grabSomething(self):
        pass

# 수정 요망 (입구 좌표)
stageEntrance = [[562, HEIGHT - 626],
                 [],
                 [],
                 [],
                 []]
stage = 0

class Zombie:

    frame = 0
    line = 0
    birthingTime = 0
    xPos = 0
    yPos = 0
    xDir = 0
    yDir = 0
    state = 'birth'

    def __init__(self):
        # gender = random.randint(0, 2)
        # if gender == 0:
        self.image = load_image("character\\girlZombieSprite.png")
        self.BirthImage = load_image("character\\GirlZombiebirthSprite.png")
        self.xPos = random.randint(100, 850)
        self.yPos = random.randint(10, 130)
        # else:
        #     self.image = load_image("character\\boyZombieSprite.png")

    def zombieBirth(self):
        self.frame = (self.birthingTime // 5) % 4
        self.line = self.birthingTime // 20
        self.BirthImage.clip_draw(105 * self.frame, 420 - 130 - 130 * self.line, 105, 130, self.xPos, self.yPos)
        self.birthingTime = self.birthingTime + 1
        if self.birthingTime >= 60:
            self.state = 'walk'
            self.line = 0
            self.frame = 0

    def walkToCafe(self):
        global stage

        if self.yPos > stageEntrance[stage][1]:
            self.state = 'check'
            self.line = 0
            self.frame = 0
            self.xDir = 0
            self.yDir = 0
            return

        if self.xPos < stageEntrance[stage][0] - 20:
            self.xDir = 1
            self.line = 3
        elif self.xPos > stageEntrance[stage][0] + 20:
            self.xDir = -1
            self.line = 2
        elif self.yPos < stageEntrance[stage][1]:
            self.xDir = 0
            self.yDir = 1
            self.line = 1
        


    def checkTable(self):
        pass

    def readyToOrder(self):
        pass

    def waitingOrder(self):
        pass

    def ThanksBye(self):
        pass

    def FailServe(self):
        pass

    def logic(self):
        match self.state:
            case 'walk':
                self.walkToCafe()
            case 'check':
                pass

        self.xPos += 6 * self.xDir 
        self.yPos += 6 * self.yDir 

    def draw(self):
        if self.state == 'birth':
            self.zombieBirth()
        else:
            self.image.clip_draw(105 * (self.frame // 4), 480 - 120 - 120 * self.line, 105, 120, self.xPos, self.yPos)
            self.frame = (self.frame + 1) % 16


pinn = None
background = None
kitchenTable = None
table = None
wall = None
bubbleBean = None
bubbleBlood = None
zombies = [None]

def enter():
    global pinn, background, kitchenTable, table, wall, bubbleBean, bubbleBlood 
    pinn = Pinn()
    zombies[0] = Zombie()
    background = load_image('map\\map.png')
    kitchenTable = load_image("map\\kitchenTable.png")
    wall = load_image('map\\wall.png')
    table = load_image('map\\table.png')
    bubbleBean = load_image('order\\bubble\\bean.png')
    bubbleBlood = load_image('order\\bubble\\blood.png')

def update():
    pinn.LineSet()
    pinn.logic()
    for zombie in zombies:
        zombie.logic()


def handle_events():
    pinn.handle_events()

def draw():
    clear_canvas()
    background.draw(WIDTH // 2, HEIGHT // 2)
    pinn.draw()
    wall.draw(230 + 626 // 2, HEIGHT - 253 - 424 // 2)
    for zombie in zombies:
        zombie.draw()
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
