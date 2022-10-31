from std import *
from pico2d import *
from pinnClass import *
from zombieClass import *
from objectClass import *
import game_framework


def enter():

    for i in range(18):
        mapping[0][i] = 1
        mapping[10][i] = 1
    for i in range(11):
        mapping[i][0] = 1
        mapping[i][17] = 1

    global pinn, background
    background = load_image('map\\map.png')
    pinn = Pinn()

    global zombies
    zombies = [Zombie()]

    global wall
    wall = objectCoordi(230, 601, 626, 76, 'map\\wall.png')

    global bloodAmericano, Latte
    bloodAmericano = load_image('order\\bloodAmericano.png')
    Latte = load_image('order\\Latte.png')

    global kitchenTables, tables, chairs, milkBox, cuptablesSmall, trashes, machines, blood
    kitchenTables = [[objectIndex(3, 4, 9, 1, 306, 72, "map\\kitchenTable.png"),
                      objectIndex(10, 0, 2, 5, 46, 197, "map\\kitchenTableright.png")]]
    tables = [objectIndex(12, 1, 2, 2, 63, 65,  'map\\table.png'),
              objectIndex(12, 6, 2, 2, 63, 65,  'map\\table.png')]
    chairs = [objectIndex(14, 1, 2, 1, 60, 90, 'map\\chair.png'),
              objectIndex(14, 6, 2, 1, 60, 90, 'map\\chair.png')]
    trashes = [objectIndex(2, 4, 1, 1, 35, 59, 'map\\trash.png')]
    machines = [objectIndex(0, 0, 2, 1, 53, 120, 'map\\machine.png', "order\\bubble\\coffeebubbleSprite.png")]
    blood = [objectIndex(2, 0, 2, 1, 46, 156, 'map\\water.png', 'order\\bubble\\bloodbubbleSprite.png')]
    milkBox = [objectIndex(4, 0, 2, 1, 51, 89, 'map\\milkBox.png', 'order\\bubble\\milkbubbleSprite.png')]
    cuptablesSmall = [objectIndex(8, 0, 2, 1, 62, 109, 'map\\cuptableSmall.png', 'order\\bubble\\coffeebubble.png', 60)]


def update():
    pinn.update()
    for zombie in zombies:
        zombie.update()
        if zombie.yPos < 0:
            del zombie
    global zombieSpawn
    zombieSpawn -= 1
    if zombieSpawn <= 0:
        zombies.append(Zombie())
        zombieSpawn = 100


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT or event.key == SDLK_ESCAPE:
            game_framework.quit()
        else:
            pinn.handle_events(event)



def draw():
    clear_canvas()
    background.draw(WIDTH // 2, HEIGHT // 2)

    # 오브젝트 y 값으로 정렬 후 출력
    yPosition = [pinn, wall]

    for trash in trashes:
        yPosition.append(trash)
    for b in blood:
        yPosition.append(b)

    for milk in milkBox:
        yPosition.append(milk)

    for cuptableSmall in cuptablesSmall:
        yPosition.append(cuptableSmall)

    for machine in machines:
        yPosition.append(machine)

    for kitchenTable in kitchenTables:
        yPosition.append(kitchenTable[0])
        yPosition.append(kitchenTable[1])

    for table in tables:
        yPosition.append(table)

    for chair in chairs:
        yPosition.append(chair)

    # for zombie in zombies:
    #     yPosition.append(zombie)


    yPosition.sort(reverse=True, key=lambda c:c.down)

    for obj in yPosition:
        obj.draw()


    global bubbleframe  # bubbleframe은 평소에 0임. 3을 바라보면 말풍선이 생긴다.
    row = int(HEIGHT - pinn.y - mapstartY) // 35 + Looking[pinn.stop][0]
    col = int(pinn.x - mapstartX) // 35 + Looking[pinn.stop][1]
    if type(mapping[row][col]) == objectIndex:
        mapping[row][col].drawBubble(bubbleframe)
        if bubbleframe < 2:
            bubbleframe += 1

    else:
        bubbleframe = 0

    # for index, menu in enumerate(menuQueue):
    #     if QueueTime[index] > -100:
    #         QueueTime[index] -= 15
    #     match menu:
    #         case 'bloodAme':
    #             bloodAmericano.draw(100 + index * 173, HEIGHT + QueueTime[index])
    #         case 'Latte':
    #             Latte.draw(100 + index * 173, HEIGHT + QueueTime[index])

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
