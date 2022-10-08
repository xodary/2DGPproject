from pico2d import *
import math

WIDTH, HEIGHT = 1200, 822

mapping = [[1, 1, 1, 1, 1, 1, 0, 0],
           [0, 0, 0, 0, 0, 1, 0, 2],
           [0, 0, 0, 0, 0, 1, 0, 0],
           [0, 0, 0, 0, 0, 1, 0, 0],
           [0, 1, 1, 1, 1, 1, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 2],
           [0, 0, 0, 0, 0, 0, 0, 0]]


class Pinn:
    stopMoving = True
    frame = 0
    x = WIDTH // 2 - 100
    y = HEIGHT // 2 + 50
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
        if self.y > HEIGHT - 431 - 72:
            global kitchenTable
            kitchenTable.draw(366 + 257 // 2 + 1, HEIGHT - 431 - 72 // 2)
    #         Table 전체 그리는게 좋을 듯
    def next_move(self):
        if self.dirX * self.dirY != 0:
            self.x += self.dirX * 15 * (1 / math.sqrt(2))
            self.y += self.dirY * 15 * (1 / math.sqrt(2))
        else:
            self.x += self.dirX * 15
            self.y += self.dirY * 15
        global mapping
        global HEIGHT
        if (self.x - 264) // 70 < 0 or (
                self.x - 264) // 70 > 7 or (
                HEIGHT - self.y - 328) // 35 < 0 or (
                HEIGHT - self.y - 328) // 35 > 7 or (
                mapping[int(HEIGHT - self.y - 328) // 35][int(self.x - 264) // 70] != 0):
            self.x = self.oldX
            self.y = self.oldY
        else:
            self.oldX = self.x
            self.oldY = self.y


open_canvas(WIDTH, HEIGHT)
background = load_image('map\\map-Recovered-Recovered.png')
kitchenTable = load_image("map\\kitchenTable.png")
running = True
pinn = Pinn()

while running:
    clear_canvas()
    background.draw(WIDTH // 2, HEIGHT // 2)
    pinn.handle_events()
    pinn.LineSet()
    pinn.next_move()
    pinn.draw()
    update_canvas()

    delay(0.07)

close_canvas()
