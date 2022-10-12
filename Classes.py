import Map
import random
from pico2d import *

running = True
class Pinn:
    stopMoving = True
    frame = 0
    x = Map.WIDTH // 2 - 100
    y = Map.HEIGHT // 2 + 50
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
                global running
                running = False
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
            self.character.clip_draw(self.stop * 23 * 4, (315 - 35 * (self.line + 1)) * 4, 23 * 4, 34 * 4, self.x,
                                     self.y + 34 * 2 - 25)
        elif not self.stopMoving:
            self.character.clip_draw(self.frame * 23 * 4, (315 - 35 * (self.line + 1)) * 4, 23 * 4, 34 * 4, self.x,
                                     self.y + 34 * 2 - 25)
            self.frame = (self.frame + 1) % 6
        if self.y > Map.HEIGHT - 431 - 72:
            global kitchenTable
            kitchenTable.draw(366 + 257 // 2 + 1, Map.HEIGHT - 431 - 72 // 2)

    def logic(self):
        if self.dirX * self.dirY != 0:
            self.x += self.dirX * 15 * (1 / math.sqrt(2))
            self.y += self.dirY * 15 * (1 / math.sqrt(2))
        else:
            self.x += self.dirX * 15
            self.y += self.dirY * 15
        if (self.x - 264) // 70 < 0 or (
                self.x - 264) // 70 > 7 or (
                Map.HEIGHT - self.y - 328) // 35 < 0 or (
                Map.HEIGHT - self.y - 328) // 35 > 7 or (
                Map.mapping[int(Map.HEIGHT - self.y - 328) // 35][int(self.x - 264) // 70] != 0):
            self.x = self.oldX
            self.y = self.oldY
        else:
            self.oldX = self.x
            self.oldY = self.y
    def grabSomething(self):
        pass


class zombie:
    def __init__(self):
        gender = random.randint(0, 2)
        if gender == 0:
            image = load_image("character\\girlZombieSprite.png")
        else:
            image = load_image("character\\boyZombieSprite.png")

    def zombieBirth(self):
        pass

    def walkToCafe(self):
        pass

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

pinn = None
background = None
kitchenTable = None

def enter():
    global pinn, background, kitchenTable
    pinn = Pinn()
    background = load_image('map\\map-Recovered-Recovered.png')
    kitchenTable = load_image("map\\kitchenTable.png")

def update():
    pinn.LineSet()
    pinn.logic()

def handle_events():
    pinn.handle_events()

def draw():
    clear_canvas()
    background.draw(Map.WIDTH // 2, Map.HEIGHT // 2)
    pinn.draw()
    update_canvas()
    delay(0.05)

def exit():
    global pinn
    del pinn

