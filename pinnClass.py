from std import *
import zombieClass
from cupClass import *

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
    cupBubble = None


    def __init__(self):
        self.character = load_image('character\\pinn.png')
        self.coffee = load_image('order\\bubble\\bean.png')
        self.blood = load_image('order\\bubble\\blood.png')
        self.milk = load_image('order\\bubble\\milkbubble.png')
        self.cupBubble = load_image('order\\bubble\\cup.png')

    def handle_events(self):
        raw = int(HEIGHT - self.y - mapstart[stage][1]) // 35 + Looking[self.stop][0]
        col = int(self.x - mapstart[stage][0]) // 35 + Looking[self.stop][1]
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

                    # 만약 좀비를 누르면 그 좀비가 레디 상태 인지 체크
                    if type(mapping[raw][col]) is zombieClass.Zombie:
                        if mapping[raw][col].state == 'ready':
                            menuQueue.append(mapping[raw][col].menu)
                            QueueTime.append(113)
                            mapping[raw][col].state = 'wait'
                        #좀비가 wait 상태이고 컵을 플레이어가 들고있으면 평가들어감
                        elif mapping[raw][col].state == 'wait' and \
                            self.item == 'cup':
                            # 음료의 성공 여부를 좀비에게 전달.
                            mapping[raw][col].DrinkCoffee(self.cup.checkCup(mapping[raw][col].menu))
                            self.cup = None
                            self.item = None


                    # 만약 컵을 누르면
                    elif type(mapping[raw][col]) == Cup:
                        if self.item != 'cup' and self.item is not None:
                            mapping[raw][col].putItem(self.item)
                            self.item = None
                        elif self.item is None:
                            self.cup = mapping[raw][col]
                            self.item = 'cup'
                            mapping[self.cup.yIndex][self.cup.xIndex] = 1
                            cups.remove(self.cup)
                        elif self.item == 'cup':    # swap
                            temp = mapping[raw][col]
                            cups.remove(temp)
                            self.cup.yIndex = raw
                            self.cup.xIndex = col
                            mapping[raw][col] = self.cup
                            cups.append(self.cup)
                            self.cup = temp
                    else:
                        match mapping[raw][col]:

                            case 'shot':
                                if self.item is None:
                                    self.item = 'shot'
                            case 'blood':
                                if self.item is None:
                                    self.item = 'blood'
                            case 'milk':
                                if self.item is None:
                                    self.item = 'milk'
                            case 'cup1':
                                if self.item is None:
                                    self.item = 'cup'
                                    self.cup = Cup()
                            case 'cup2':
                                if self.item is None:
                                    self.item = 'cup'
                                    self.cup = Cup()
                            case 'trash':
                                self.item = None
                            case 1:
                                if self.item == 'cup':
                                    self.cup.yIndex = raw
                                    self.cup.xIndex = col
                                    mapping[self.cup.yIndex][self.cup.xIndex] = self.cup
                                    cups.append(self.cup)
                                    self.cup = None
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

    def logic(self):
        # 대각선 이동

        if self.dirX * self.dirY != 0:
            self.x += self.dirX * 15 * (1 / math.sqrt(2))
            self.y += self.dirY * 15 * (1 / math.sqrt(2))
        else:
            self.x += self.dirX * 15
            self.y += self.dirY * 15
        raw = int(HEIGHT - self.y - mapstart[stage][1]) // 35
        colLeft = int(self.x - mapstart[stage][0] - 20) // 35
        colRight = int(self.x - mapstart[stage][0] + 20) // 35
        if mapping[raw][colLeft] != 0 or mapping[raw][colRight] != 0:
            self.x = self.oldX
            self.y = self.oldY
        else:
            self.oldX = self.x
            self.oldY = self.y
        self.LineSet()

