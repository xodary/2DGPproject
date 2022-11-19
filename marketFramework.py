
from std import *
from pico2d import *
import pinnClass
# from zombieClass import *
from objectClass import *
import AllObjectClass
import game_framework
import gamePlay
import marketClass


itemImages = []
selling = []
Menu = None
mouseOn = None
Buttons = []
sellingPoint = None
button = 0
x, y = 0, 0
def enter():
    global Menu
    Menu = marketClass.MarketUI_Background()
    AllObjectClass.add_object(Menu, 4)
    global selling, Buttons
    cup = marketClass.OrderBox('UI\\cupSell.png', 'UI\\cupBigIcon.png', 'UI\\cupSmallIcon.png',
                               189, 270, 750, 121, 1, 1)
    milk = marketClass.OrderBox('UI\\milkSell.png', 'UI\\milkBigIcon.png', 'UI\\milkSmallIcon.png',
                                189, 735, 750, 230, 1, 2)
    machine = marketClass.OrderBox('UI\\machineSell.png', 'UI\\machineBigIcon.png', 'UI\\machineSmallIcon.png',
                                   189, 408, 750, 300, 1, 2)
    bin = marketClass.OrderBox('UI\\orderBin.png', 'UI\\binBigIcon.png', 'UI\\binSmallIcon.png',
                               189, 270, 749, 147, 1, 1)
    shelf = marketClass.OrderBox('UI\\orderShelf.png', 'UI\\shelfBigIcon.png', 'UI\\shelfSmallIcon.png',
                                 189, 450, 749, 211, 2, 2)
    table = marketClass.OrderBox('UI\\orderTable.png', 'UI\\tableBigIcon.png', 'UI\\tableSmallIcon.png',
                                 189, 700, 749, 197, 3, 2)
    blood = marketClass.OrderBox('UI\\orderBlood.png', 'UI\\bloodBigIcon.png', 'UI\\bloodSmallIcon.png',
                                 189, 270, 749, 293, 1, 2)
    tree = marketClass.OrderBox('UI\\orderFingerTree.png', 'UI\\treeBigIcon.png', 'UI\\treeSmallIcon.png',
                                 189, 600, 749, 302, 3, 3)
    kitchenTable = marketClass.OrderBox('UI\\orderKitchenTable.png', 'UI\\kitchenTableBigIcon.png', 'UI\\kitchenTableSmallIcon.png',
                                 189, 1000, 749, 295, 3, 2)
    cow = marketClass.OrderBox('UI\\orderCow.png', 'UI\\cowBigIcon.png', 'UI\\cowTableSmallIcon.png',
                                 189, 270, 749, 182, 3, 2)
    chicken = marketClass.OrderBox('UI\\orderChicken.png', 'UI\\chickenBigIcon.png', 'UI\\chickenTableSmallIcon.png',
                               189, 500, 749, 137, 3, 2)
    Buttons = [marketClass.Button(0), marketClass.Button(1), marketClass.Button(2)]
    AllObjectClass.add_objects(Buttons, 5)
    furniture = []
    furniture.append([cup, milk, machine])
    furniture.append([bin, shelf, table])
    furniture.append([blood, tree, kitchenTable])
    selling.append(furniture)

    animal = []
    animal.append([cow, chicken])
    selling.append(animal)
    Menu.GetItems(selling[sellingPoint], Buttons)

def update():
    # for object in AllObjectClass.all_objects():
    #     object.update()
    if mouseOn:
        mouseOn.x, mouseOn.y = x, y

def handle_events():
    global mouseOn
    global x, y
    global button
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_MOUSEBUTTONDOWN or \
                event.type == SDL_MOUSEMOTION or\
                event.type == SDL_MOUSEBUTTONUP:
            x, y = event.x, gamePlay.HEIGHT - event.y
            if event.type == SDL_MOUSEBUTTONDOWN:
                mouseOn = Menu.MouseButtonDown(x, y)
            elif event.type == SDL_MOUSEMOTION:
                Menu.MouseMotion(x, y, mouseOn)
            elif event.type == SDL_MOUSEBUTTONUP:
                Menu.MouseButtonUp(mouseOn)
                mouseOn = None
        elif event.key == SDLK_ESCAPE:
            gamePlay.pinn.handle_events(event)
            game_framework.pop_state()

def draw():

    clear_canvas()
    for object in AllObjectClass.all_objects():
        object.draw()

    update_canvas()

def exit():
    Menu.exit()
    for menu in selling.copy():
        selling.remove(menu)
    AllObjectClass.remove_object(Menu)
    for itemImage in itemImages.copy():
        AllObjectClass.remove_object(itemImage)
        itemImages.remove(itemImage)
    if mouseOn != None:
        AllObjectClass.remove_object(mouseOn)
    for Button in Buttons:
        AllObjectClass.remove_object(Button)

def pause():
    pass

def resume():
    pass

def test_self():
    import sys
    this_module = sys.modules['__main__']
    pico2d.open_canvas(1920, 1280)
    game_framework.run(this_module)
    pico2d.close_canvas()


if __name__ == '__main__':
    test_self()