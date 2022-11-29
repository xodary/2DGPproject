
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



    #  orderBoxImage: {encode},
    # bigIconImage: {encode},
    # smallIconImage: {encode},
    # furnitureImage: Any,
    # orderLeft: {__add__},
    # orderRight: {__add__},
    # orderWidth: {__truediv__},
    # orderHeight: {__truediv__},
    # weightX: Any,
    # weightY: Any,
    # weightMapX: Any,
    # weightMapY: Any,
    # furnitureWidth: Any,
    # furnitureHeight: Any,
    # weightList: Any = None,
    # weightMapList: Any = None) -> None
    # cup = marketClass.Myitem('UI\\cupSell.png', 'UI\\cupBigIcon.png', 'UI\\cupSmallIcon.png',
    #                            189, 270, 750, 121, 1, 1)
    milk = marketClass.Myitem('UI\\milkSell.png', 'UI\\milkBigIcon.png',
                              'UI\\milkSmallIcon.png', 'map1.6\\milkBox.png',
                               189, 735, 750, 230, 1, 2, 2, 1, 81, 142, bubbleImage='bubble\\milk.png')
    machine = marketClass.Myitem('UI\\machineSell.png', 'UI\\machineBigIcon.png',
                                 'UI\\machineSmallIcon.png', 'map1.6\\machine.png',
                                   189, 408, 750, 300, 1, 2, 2, 1, 84, 194, bubbleImage="bubble\\coffee.png")
    bin = marketClass.Myitem('UI\\orderBin.png', 'UI\\binBigIcon.png', 'UI\\binSmallIcon.png', 'map1.6\\trash.png',
                               189, 270, 749, 147, 1, 1, 1, 1, 56, 94, )
    shelf = marketClass.Myitem('UI\\orderShelf.png', 'UI\\shelfBigIcon.png',
                               'UI\\shelfSmallIcon.png', 'map1.6\\cuptableSmall.png',
                               189, 450, 749, 211, 2, 2, 2, 1, 99, 174, bubbleImage='bubble\\cup.png')
    tableList = [
        [1,1,0],
        [1,1,1]
    ]

    # table 가구 이미지 변경(의자랑 합치기)
    table = marketClass.Myitem('UI\\orderTable.png', 'UI\\tableBigIcon.png',
                               'UI\\tableSmallIcon.png', 'map1.6\\table.png',
                                 189, 700, 749, 197, 3, 2, 2, 2, 100, 104, tableList)
    blood = marketClass.Myitem('UI\\orderBlood.png', 'UI\\bloodBigIcon.png', 'UI\\bloodSmallIcon.png', 'map1.6\\water.png',
                                 189, 270, 749, 293, 1, 2, 2, 1, 73, 249, bubbleImage='bubble\\blood.png')
    # tree = marketClass.Myitem('UI\\orderFingerTree.png', 'UI\\treeBigIcon.png', 'UI\\treeSmallIcon.png',
    #                              189, 600, 749, 302, 3, 3,)
    kitchenTableList = [
        [0,0,1],
        [1,1,1]
    ]
    kitchenMapList = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    ]
    kitchenTable = marketClass.Myitem('UI\\orderKitchenTable.png', 'UI\\kitchenTableBigIcon.png',
                                      'UI\\kitchenTableSmallIcon.png', "map1.6\\kitchenTable.png",
                                 189, 270, 749, 295, 3, 2, 10, 5, 477, 315, kitchenTableList, kitchenMapList)
    # cow = marketClass.Myitem('UI\\orderCow.png', 'UI\\cowBigIcon.png', 'UI\\cowTableSmallIcon.png',
    #                              189, 270, 749, 182, 3, 2)
    # chicken = marketClass.Myitem('UI\\orderChicken.png', 'UI\\chickenBigIcon.png', 'UI\\chickenTableSmallIcon.png',
    #                            189, 500, 749, 137, 2, 2)
    Buttons = [marketClass.Button(0), marketClass.Button(1), marketClass.Button(2), marketClass.Button(3)]
    AllObjectClass.add_objects(Buttons, 5)
    furniture = []
    furniture.append([milk, machine])
    furniture.append([bin, shelf, table])
    furniture.append([blood])
    furniture.append([kitchenTable])
    selling.append(furniture)
    animal = []
    # animal.append([cow, chicken])
    selling.append(animal)
    Menu.GetItems(selling[sellingPoint], Buttons)

def update():
    for object in AllObjectClass.all_objects():
        object.update()

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
    if mouseOn != None:
        AllObjectClass.remove_object(mouseOn)
    for Button in Buttons:
        AllObjectClass.remove_object(Button)
    if mouseOn:
        AllObjectClass.remove_object(mouseOn)


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