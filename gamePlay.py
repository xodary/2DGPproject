from std import *
from pinnClass import *
from zombieClass import *
import game_framework
from pico2d import *
import std


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
    global bubblecup
    bubblecup = load_image('order\\bubble\\coffeebubble.png')


def update():
    pinn.logic()
    for zombie in zombies:
        zombie.logic()
        if zombie.yPos < 0:
            del zombie
    global zombieSpawn
    zombieSpawn -= 1
    if zombieSpawn <= 0:
        zombies.append(Zombie())
        zombieSpawn = 100


def handle_events():
    pinn.handle_events()


def draw():
    clear_canvas()
    background.draw(WIDTH // 2, HEIGHT // 2)


    # 오브젝트 y 값으로 정렬 후 출력
    yPosition = [Object(kitchenTable, kitchenTableCoordinate[stage][0],kitchenTableCoordinate[stage][1],False , 250, 72, HEIGHT - kitchenTableCoordinate[stage][1] - 72),
                 Object(trash, trashCoordinate[stage][0], trashCoordinate[stage][1], False, 36, 58, HEIGHT - trashCoordinate[stage][1] - 58),
                 Object(wall, wallCoordinate[stage][0],wallCoordinate[stage][1], False, 626, 424, HEIGHT - wallCoordinate[stage][1] - 424),
                 Object(pinn, compareY=pinn.y, special=True)]

    for tablecoordi in tableCoordinate[stage]:
        yPosition.append(Object(table, tablecoordi[0], tablecoordi[1], False, 64, 64,
               HEIGHT - tablecoordi[1] - 64 + 20))

    for chaircoordi in chairCoordinate[stage]:
        yPosition.append(Object(chair, chaircoordi[0], chaircoordi[1], False, 60, 90,
               HEIGHT - chaircoordi[1] - 90 + 30))

    for zombie in zombies:
        yPosition.append(Object(zombie, compareY=zombie.yPos - 10, special=True))

    yPosition.sort(reverse=True, key=lambda c:c.compareY)

    for obj in yPosition:
        match obj.special:
            case False:
                obj.name.draw(obj.x + obj.width // 2, HEIGHT - obj.y - obj.height // 2)
                if obj.name == kitchenTable:
                    for cup in cups:
                         cup.draw()
            case True:
                obj.name.draw()


    global bubbleframe  # bubbleframe은 평소에 0임. 3을 바라보면 말풍선이 생긴다.
    match mapping[int(HEIGHT - pinn.y - mapstart[stage][1]) // 35 + Looking[pinn.stop][0]][
        int(pinn.x - mapstart[stage][0]) // 35 + Looking[pinn.stop][1]]:
        case 'shot':
            bubbleBean.clip_draw(50 * bubbleframe, 0, 50, 50,
                                 bubbleBeanCoordinate[stage][0] + 50 // 2,
                                 HEIGHT - bubbleBeanCoordinate[stage][1] - 50 // 2)
            if bubbleframe < 2:
                bubbleframe = bubbleframe + 1
        case 'blood':
            bubbleBlood.clip_draw(50 * bubbleframe, 0, 50, 50,
                                  bubbleBloodCoordinate[stage][0] + 50 // 2,
                                  HEIGHT - bubbleBloodCoordinate[stage][1] - 50 // 2)
            if bubbleframe < 2:
                bubbleframe = bubbleframe + 1
        case 'milk':
            bubblemilk.clip_draw(50 * bubbleframe, 0, 50, 50,
                                 bubblemilkCoordinate[stage][0] + 50 // 2,
                                 HEIGHT - bubblemilkCoordinate[stage][1] - 50 // 2)
            if bubbleframe < 2:
                bubbleframe = bubbleframe + 1
        case 'cup1':
            bubblecup.clip_draw(60 * bubbleframe, 0, 60, 60,
                                bubblecup1Coordinate[stage][0] + 60 // 2,
                                HEIGHT - bubblecup1Coordinate[stage][1] - 60 // 2)
            if bubbleframe < 2:
                bubbleframe = bubbleframe + 1
        case 'cup2':
            bubblecup.clip_draw(60 * bubbleframe, 0, 60, 60,
                                bubblecup2Coordinate[stage][0] + 60 // 2,
                                HEIGHT - bubblecup2Coordinate[stage][1] - 60 // 2)
            if bubbleframe < 2:
                bubbleframe = bubbleframe + 1
        case _:
            bubbleframe = 0
    #
    # for zombie in zombies:
    #     if pinn.y < zombie.yPos - 20:
    #         zombie.draw()
    #         if zombie.yPos > HEIGHT - tableCoordinate[stage][1] - 65:
    #             table.draw(tableCoordinate[stage][0] + 64 // 2,
    #                        HEIGHT - tableCoordinate[stage][1] - 64 // 2)
    #         if zombie.yPos > HEIGHT - chairCoordinate[stage][1] - 90:
    #             chair.draw(chairCoordinate[stage][0] + 60 // 2, HEIGHT - chairCoordinate[stage][1] - 90 // 2)
    # pinn.draw()
    # if pinn.y - 20 > HEIGHT - kitchenTableCoordinate[stage][1] - 72:
    #     kitchenTable.draw(kitchenTableCoordinate[stage][0] + 250 // 2,
    #                       HEIGHT - kitchenTableCoordinate[stage][1] - 72 // 2)
    #     for cup in cups:
    #         cup.draw()
    # if pinn.y - 20 > HEIGHT - tableCoordinate[stage][1] - 65:
    #     table.draw(tableCoordinate[stage][0] + 63 // 2 + 1,
    #                HEIGHT - tableCoordinate[stage][1] - 65 // 2 - 1)
    # if pinn.y - 20 > HEIGHT - chairCoordinate[stage][1] - 90:
    #     chair.draw(chairCoordinate[stage][0] + 60 // 2, HEIGHT - chairCoordinate[stage][1] - 90 // 2)
    # if pinn.y - 20 > HEIGHT - trashCoordinate[stage][1] - 59:
    #     trash.draw(trashCoordinate[stage][0] + 36 // 2, HEIGHT - trashCoordinate[stage][1] - 58 // 2)
    # wall.draw(wallCoordinate[stage][0] + 626 // 2, HEIGHT - wallCoordinate[stage][1] - 424 // 2)
    # for zombie in zombies:
    #     if pinn.y > zombie.yPos - 20:
    #         zombie.draw()
    #         if zombie.yPos > HEIGHT - tableCoordinate[stage][1] - 65:
    #             table.draw(tableCoordinate[stage][0] + 63 // 2 + 1, HEIGHT - tableCoordinate[stage][1] - 65 // 2 - 1)
    #         if zombie.yPos > HEIGHT - chairCoordinate[stage][1] - 90:
    #             chair.draw(chairCoordinate[stage][0] + 60 // 2, HEIGHT - chairCoordinate[stage][1] - 90 // 2)
    #         if zombie.yPos > HEIGHT - wallCoordinate[stage][1] - 424:
    #             wall.draw(wallCoordinate[stage][0] + 626 // 2, HEIGHT - wallCoordinate[stage][1] - 424 // 2)
    for index, menu in enumerate(menuQueue):
        if QueueTime[index] > -100:
            QueueTime[index] -= 15
        match menu:
            case 'bloodAme':
                bloodAmericano.draw(100 + index * 173, HEIGHT + QueueTime[index])
            case 'Latte':
                Latte.draw(100 + index * 173, HEIGHT + QueueTime[index])

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
