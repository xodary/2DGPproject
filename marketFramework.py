
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
itemList = []
Menu = None
mouseOn = None
button = 0
x, y = 0, 0
def enter():
    global Menu
    Menu = marketClass.marketUI()
    AllObjectClass.add_object(Menu, 4)
    global itemList
    cup = marketClass.marketSell('UI\\cupSell.png', 'UI\\cupmini.png', 'UI\\cupInven.png', 189, 270, 750, 121, 1, 1)
    milk = marketClass.marketSell('UI\\milkSell.png', 'UI\\cupmini.png', 'UI\\cupInven.png', 189, 735, 750, 230, 1, 2)
    machine = marketClass.marketSell('UI\\machineSell.png', 'UI\\cupmini.png', 'UI\\cupInven.png', 189, 408, 750, 300, 1, 2)
    itemList.append([cup, milk, machine])
    AllObjectClass.add_objects(itemList[button], 5)


def update():
    # for object in AllObjectClass.all_objects():
    #     object.update()
    pass

def handle_events():
    global mouseOn
    global x, y
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_MOUSEBUTTONDOWN or \
                event.type == SDL_MOUSEMOTION or\
                event.type == SDL_MOUSEBUTTONUP:
            menuL, menuR, menuB, menuT = 189, 189 + 700, gamePlay.HEIGHT - (270+695), gamePlay.HEIGHT - 270
            itemL, itemR, itemB, itemT = 1046, 1046+700, gamePlay.HEIGHT - (270+673), gamePlay.HEIGHT - 270
            x, y = event.x, gamePlay.HEIGHT - event.y
            if event.type == SDL_MOUSEBUTTONDOWN:
                # menu 칸에 클릭하면 선택함
                if menuL <= x <= menuR and menuB <= y <= menuT and mouseOn == None:
                    for item in itemList[button]:
                        if item.x - item.width / 2 < x < item.x + item.width / 2 and\
                                item.y - item.height / 2 < y < item.y + item.height / 2:
                            mouseOn = item.makeMarket(x, y)
                            AllObjectClass.add_object(mouseOn, 6)
            elif event.type == SDL_MOUSEMOTION:
                # item 쪽에 마우스 올리면 칸에 쏙 들어감
                if mouseOn is not None:
                    if itemL <= x <= itemR and itemB <= y <= itemT:
                        if mouseOn.mouseOffTest():
                            mouseOn.fit = True
                        else:
                            mouseOn.fit = False
                    else:
                        mouseOn.fit = False
                    mouseOn.x, mouseOn.y = x, y
                # menu 에 마우스 올리면 선택 대기 상태
                if menuL <= x <= menuR and menuB <= y <= menuT:
                    for item in itemList[button]:
                        if item.x - item.width / 2 < x < item.x + item.width / 2 and\
                                item.y - item.height / 2 < y < item.y + item.height / 2:
                            item.mouseOn()
                        else:
                            item.mouseOff()
            elif event.type == SDL_MOUSEBUTTONUP:
                x, y = event.x, gamePlay.HEIGHT - event.y
                if mouseOn is not None:
                    if mouseOn.mouseOffTest():
                        mouseOn.success()
                        itemImages.append(mouseOn)
                    else:
                        AllObjectClass.remove_object(mouseOn)
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
    for items in itemList.copy():
        for item in items:
            AllObjectClass.remove_object(item)
        itemList.remove(items)
    AllObjectClass.remove_object(Menu)
    for itemImage in itemImages.copy():
        AllObjectClass.remove_object(itemImage)
        itemImages.remove(itemImage)
    if mouseOn != None:
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