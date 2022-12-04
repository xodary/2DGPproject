import recipeClass
from std import *
from pico2d import *
import pinnClass
# from zombieClass import *e
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
kitchenTables = None
tables = None
chairs = None
trashes = None
machines = None
bloods = None
milkBoxes = None
cuptablesSmall = None
trees = None
cow = None
chicken = None

def enter():
    global Menu
    Menu = marketClass.MarketUI_Background()
    AllObjectClass.add_object(Menu, 4)
    global selling, Buttons


    global kitchenTables, tables, chairs, trashes, machines, bloods, milkBoxes, cuptablesSmall, trees, cow, chicken

    trees = marketClass.noWait('UI\\orderFingerTree.png', 'UI\\treeBigIcon.png',
                               'UI\\treeSmallIcon.png', 'map1.6\\fingerTree.png',
                               186, 600, 749, 302, 3, 3, 2, 2, 182, 269, 20,
                               bgm='sound\\tree.wav', bubbleImage='bubble\\finger.png')
    milkBoxes = marketClass.noWait('UI\\milkSell.png', 'UI\\milkBigIcon.png',
                                   'UI\\milkSmallIcon.png', 'map1.6\\milkBox.png',
                                   189, 700, 750, 230, 1, 2, 3, 1, 81, 142, 10,
                                   bgm='sound\\milk.wav', bubbleImage='bubble\\milk.png')
    machines = marketClass.waitingForSecond('UI\\machineSell.png', 'UI\\machineBigIcon.png',
                                            'UI\\machineSmallIcon.png', 'map1.6\\machine.png',
                                            189, 300, 750, 300, 1, 2, 3, 1, 84, 194, 10,
                                            bgm='sound\\machine.wav', bubbleImage="bubble\\coffee.png")
    trashes = marketClass.Myitem('UI\\orderBin.png', 'UI\\binBigIcon.png', 'UI\\binSmallIcon.png', 'map1.6\\trash.png',
                                 189, 270, 749, 147, 1, 1, 2, 1, 56, 94, 4, )
    cuptablesSmall = marketClass.noWait('UI\\orderShelf.png', 'UI\\shelfBigIcon.png',
                                        'UI\\shelfSmallIcon.png', 'map1.6\\cuptableSmall.png',
                                        189, 450, 749, 211, 2, 2, 3, 1, 99, 174, 10,
                                        bgm='sound\\cup.wav', bubbleImage='bubble\\cup.png')
    tableList = [
        [1, 1, 0],
        [1, 1, 1]
    ]

    # table 가구 이미지 변경(의자랑 합치기)
    tables = marketClass.Table('UI\\orderTable.png', 'UI\\tableBigIcon.png',
                               'UI\\tableSmallIcon.png', 'map1.6\\tableandchair.png',
                               189, 700, 749, 197, 3, 2, 8, 1, 216, 147, 10,
                               weightList=tableList)
    bloods = marketClass.waitingForSecond('UI\\orderBlood.png', 'UI\\bloodBigIcon.png', 'UI\\bloodSmallIcon.png',
                                          'map1.6\\water.png',
                                          189, 270, 749, 293, 1, 2, 3, 1, 73, 249, 10,
                                          bgm='sound\\water.wav', bubbleImage='bubble\\blood.png')
    kitchenTableList = [
        [0, 0, 1],
        [1, 1, 1]
    ]
    kitchenMapList = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    ]
    kitchenTables = marketClass.Myitem('UI\\orderKitchenTable.png', 'UI\\kitchenTableBigIcon.png',
                                       'UI\\kitchenTableSmallIcon.png', "map1.6\\kitchenTable.png",
                                       189, 270, 749, 295, 3, 2, 18, 5, 477, 315, 20,
                                       weightList=kitchenTableList, weightMapList=kitchenMapList)
    cow = marketClass.Animal('UI\\orderCow.png', 'UI\\cowBigIcon.png',
                             'UI\\cowSmallIcon.png', 'character1.6\\cow.png',
                             189, 270, 749, 182, 3, 2, 0, 0, 256, 256, 15, bgm='sound\\cow.wav')
    chicken = marketClass.Animal('UI\\orderChicken.png', 'UI\\chickenBigIcon.png',
                                 'UI\\chickenSmallIcon.png', 'character1.6\\chicken.png',
                                 189, 500, 749, 137, 2, 2, 0, 0, 128, 128, 10, bgm='sound\\chicken.wav')
    latte = recipeClass.Recipe('order\\latterecipe.png', 189, 700, 189 + 750, 700 + 300, 20, 'order\\Latte.png', 2)
    egglatte = recipeClass.Recipe('order\\egglatterecipe.png', 189, 300, 189 + 750, 300 + 300, 30, 'order\\eggLatte.png', 3)
    fraffe = recipeClass.Recipe('order\\frafferecipe.png', 189, 700, 189 + 750, 700 + 300, 40, 'order\\finger.png', 4)
    Buttons = [[marketClass.Button(0), marketClass.Button(1), marketClass.Button(2), marketClass.Button(3)],
               [marketClass.Button(0)],
               [marketClass.Button(0), marketClass.Button(1)]]
    AllObjectClass.add_objects(Buttons[sellingPoint], 5)
    furniture = []
    furniture.append([milkBoxes, machines])
    furniture.append([trashes, cuptablesSmall, tables])
    furniture.append([bloods, trees])
    furniture.append([kitchenTables])
    selling.append(furniture)
    animal = []
    animal.append([cow, chicken])
    selling.append(animal)
    recipe = []
    recipe.append([latte, egglatte])
    recipe.append([fraffe])
    selling.append(recipe)
    Menu.GetItems(selling[sellingPoint], Buttons[sellingPoint])


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
                event.type == SDL_MOUSEMOTION or \
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
    for Button in Buttons[sellingPoint]:
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
