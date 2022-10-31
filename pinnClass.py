from std import *
from pico2d import *
import zombieClass
import cupClass
import objectClass

running = True


class Pinn:
    pinnImage = 'character\\pinn.png'
    pinnImageX = 92
    pinnImageY = 140
    coffee = 'order\\bubble\\bean.png'
    blood = 'order\\bubble\\blood.png'
    milk = 'order\\bubble\\milkbubble.png'
    cupBubble = 'order\\bubble\\cup.png'

    def __init__(self):
        self.character = load_image(Pinn.pinnImage)
        self.stopMoving = True
        self.frame = 0
        self.x = WIDTH // 2 - 100
        self.y = HEIGHT // 2
        self.down = self.y - 40
        self.oldX = self.x
        self.oldY = self.y
        self.dirX = 0
        self.dirY = 0
        self.line = 0
        self.stop = 0
        self.item = None

    def handle_events(self, event):
        raw = int(HEIGHT - self.y - mapstartY) // 35 + Looking[self.stop][0]
        col = int(self.x - mapstartX) // 35 + Looking[self.stop][1]

        if event.type == SDL_KEYDOWN:
            self.stopMoving = False
            if event.key == SDLK_RIGHT:
                self.dirX += 1
            elif event.key == SDLK_LEFT:
                self.dirX -= 1
            elif event.key == SDLK_UP:
                self.dirY += 1
            elif event.key == SDLK_DOWN:
                self.dirY -= 1
            elif event.key == SDLK_SPACE:
                pass
                # object = mapping[raw][col]


                # match type(object):
                #     case zombieClass.Zombie:
                #         if mapping[raw][col].cur_state == zombieClass.READY:
                #             menuQueue.append(mapping[raw][col].menu)
                #             QueueTime.append(113)
                #             mapping[raw][col].add_state(zombieClass.WAIT)
                #         #좀비가 wait 상태이고 컵을 플레이어가 들고있으면 평가들어감
                #         elif mapping[raw][col].cur_state == zombieClass.WAIT and \
                #             self.item == 'cup':
                #             # 음료의 성공 여부를 좀비에게 전달.
                #             mapping[raw][col].cur_state(self.cup.checkCup(mapping[raw][col].menu))
                #             self.cup = None
                #             self.item = None
                #     case cupClass.Cup:
                #         if self.item != 'cup' and self.item is not None:
                #             mapping[raw][col].putItem(self.item)
                #             self.item = None
                #         elif self.item is None:
                #             self.cup = mapping[raw][col]
                #             self.item = 'cup'
                #             mapping[self.cup.yIndex][self.cup.xIndex] = 1
                #             cups.remove(self.cup)
                #         elif self.item == 'cup':    # swap
                #             temp = mapping[raw][col]
                #             cups.remove(temp)
                #             self.cup.yIndex = raw
                #             self.cup.xIndex = col
                #             mapping[raw][col] = self.cup
                #             cups.append(self.cup)
                #             self.cup = temp
                #     case objectClass.objectIndex:
                #         self.item = mapping[raw][col].spacebar()
                #         if mapping[raw][col] in trashes:
                #             self.item = None
                #         if self.item == 'cup':
                #             self.cup.yIndex = raw
                #             self.cup.xIndex = col
                #             mapping[self.cup.yIndex][self.cup.xIndex] = self.cup
                #             cups.append(self.cup)
                #             self.cup = None
                #             self.item = None

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
        match (self.dirX, self.dirY):
            case (1, 1):
                self.line = 8
                self.stop = 3
            case (-1, 1):
                self.line = 7
                self.stop = 5
            case (-1, -1):
                self.line = 2
                self.stop = 7
            case (1, -1):
                self.line = 3
                self.stop = 1
            case (0, 1):
                self.line = 6
                self.stop = 4
            case (0, -1):
                self.line = 1
                self.stop = 0
            case (1, 0):
                self.line = 5
                self.stop = 2
            case (-1, 0):
                self.line = 4
                self.stop = 6
            case (0, 0):
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
        if self.item is not None:
            match self.item:
                case 'shot':
                    self.coffee.draw(self.x, self.y + 130)
                case 'blood':
                    self.blood.draw(self.x, self.y + 130)
                case 'milk':
                    self.milk.draw(self.x, self.y + 130)
                case 'cup':
                    self.cupBubble.draw(self.x, self.y + 140)

        # 입체감

    def update(self):
        # 대각선 이동

        self.down = self.y - 40
        if self.dirX * self.dirY != 0:
            self.x += self.dirX * 15 * (1 / math.sqrt(2))
            self.y += self.dirY * 15 * (1 / math.sqrt(2))
        else:
            self.x += self.dirX * 15
            self.y += self.dirY * 15
        rawTop = int(HEIGHT - self.y - mapstartY + 10) // 35
        rawBottom = int(HEIGHT - self.y - mapstartY - 10) // 35
        colLeft = int(self.x - mapstartX - 20) // 35
        colRight = int(self.x - mapstartX + 20) // 35
        if mapping[rawTop][colLeft] != 0 or mapping[rawTop][colRight] != 0 or\
            mapping[rawBottom][colLeft] != 0 or mapping[rawBottom][colRight] != 0:
            self.x = self.oldX
            self.y = self.oldY
        else:
            self.oldX = self.x
            self.oldY = self.y
        self.LineSet()

