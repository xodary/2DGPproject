from std import *
from pico2d import *
from pinnClass import *
# from zombieClass import *
from objectClass import *
import AllObjectClass
import game_framework


def enter():

    # global pinn
    # background = BackGround('map\\mapBig.png')
    # AllObjectClass.add_object(background, 0)
    # pinn = Pinn()
    # AllObjectClass.add_object(pinn, 1)
    #
    # # global zombies
    # # zombies = [Zombie()]
    #
    # AllObjectClass.add_object(WALL(630, 253, 626, 75, 'map\\walltop.png'), 1)
    #
    # AllObjectClass.add_object(WALL(630, 603, 626, 76, 'map\\wall.png'), 1)
    #
    # AllObjectClass.add_object(WALL(0, HEIGHT - 61, 1600, 61, 'map\\fence.png'), 1)
    #
    # AllObjectClass.add_object(fire(1478, 853, 40, 70, 'map\\fire.png'), 1)
    #
    # # global bloodAmericano, Latte
    # # bloodAmericano = load_image('order\\bloodAmericano.png')
    # # Latte = load_image('order\\Latte.png')
    #
    # kitchenTables = [[interactionTOOL(3, 4, 8, 1, 253, 72, "map\\kitchenTable.png"),
    #                   interactionTOOL(10, 0, 2, 5, 46, 197, "map\\kitchenTableright.png")]]
    # for t in kitchenTables:
    #     AllObjectClass.add_objects(t, 1)
    # tables = [TABLE(12, 1, 2, 2, 63, 65,  'map\\table.png'),
    #           TABLE(12, 6, 2, 2, 63, 65,  'map\\table.png')]
    # AllObjectClass.add_objects(tables, 1)
    # chairs = [interactionTOOL(14, 1, 2, 1, 60, 90, 'map\\chair.png'),
    #           interactionTOOL(14, 6, 2, 1, 60, 90, 'map\\chair.png')]
    # AllObjectClass.add_objects(chairs, 1)
    # trashes = [interactionTOOL(2, 4, 1, 1, 35, 59, 'map\\trash.png')]
    # AllObjectClass.add_objects(trashes, 1)
    # machines = [interactionTOOL(0, 0, 2, 1, 53, 120, 'map\\machine.png', "order\\bubble\\coffeebubbleSprite.png")]
    # AllObjectClass.add_objects(machines, 1)
    # blood = [interactionTOOL(2, 0, 2, 1, 46, 156, 'map\\water.png', 'order\\bubble\\bloodbubbleSprite.png')]
    # AllObjectClass.add_objects(blood, 1)
    # milkBox = [interactionTOOL(4, 0, 2, 1, 51, 89, 'map\\milkBox.png', 'order\\bubble\\milkbubbleSprite.png')]
    # AllObjectClass.add_objects(milkBox, 1)
    # cuptablesSmall = [interactionTOOL(8, 0, 2, 1, 62, 109, 'map\\cuptableSmall.png', 'order\\bubble\\coffeebubble.png', 60)]
    # AllObjectClass.add_objects(cuptablesSmall, 1)

    global pinn
    background = WALL(0, 0, 1200, 800, 'map\\market.png')
    AllObjectClass.add_object(background, 0)
    pinn = Pinn()
    AllObjectClass.add_object(pinn, 1)
    AllObjectClass.add_object(WALL(21, 306, 158, 307, 'map\\christmas.png'), 1)
    AllObjectClass.add_object(WALL(499, 344, 263, 289, 'map\\animalmarket.png'), 1)
    AllObjectClass.add_object(WALL(275, 62, 242, 207, 'map\\shop.png'), 1)
    AllObjectClass.add_object(WALL(843, 49, 199, 212, 'map\\shop2.png'), 1)
    AllObjectClass.add_object(WALL(842, 356, 99, 145, 'map\\tree.png'), 1)


def update():
    for object in AllObjectClass.all_objects():
        object.update()


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT or event.key == SDLK_ESCAPE:
            game_framework.quit()
        else:
            pinn.handle_events(event)



def draw():

    clear_canvas()

    for object in AllObjectClass.all_objects():
        object.draw()



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
    pico2d.open_canvas(1200, 800)
    game_framework.run(this_module)
    pico2d.close_canvas()


if __name__ == '__main__':
    test_self()
