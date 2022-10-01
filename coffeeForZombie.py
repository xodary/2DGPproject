from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1200, 822

def handle_events():
    global running
    global dirX
    global dirY
    global line
    global stop
    global frame

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            stop = 6
            if event.key == SDLK_RIGHT:
                dirX += 1
                line = 5
            elif event.key == SDLK_LEFT:
                dirX -= 1
                line = 4
            elif event.key == SDLK_UP:
                line = 6
                dirY += 1
            elif event.key == SDLK_DOWN:
                line = 1
                dirY -= 1
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            stop = 0
            if event.key == SDLK_RIGHT:
                dirX -= 1
                line = 0
                frame = 2
            elif event.key == SDLK_LEFT:
                dirX += 1
                line = 0
                frame = 6
            elif event.key == SDLK_UP:
                line = 0
                dirY -= 1
                frame = 4
            elif event.key == SDLK_DOWN:
                line = 0
                dirY += 1
                frame = 0


open_canvas(TUK_WIDTH, TUK_HEIGHT)
grass = load_image('map\\map-Recovered-Recovered.png')
character = load_image('character\\pinn.png')

running = True
x = TUK_WIDTH // 2
y = TUK_HEIGHT // 2
frame = 0
dirX = 0
dirY = 0
line = 0
stop = 0

while running:
    clear_canvas()
    grass.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    character.clip_draw(frame * 23 * 4, (315 - 35 * (line + 1)) * 4, 23 * 4, 34 * 4, x, y)
    update_canvas()

    handle_events()
    if(stop > 0):
        frame = (frame + 1) % stop
    x += dirX * 5
    if x < 0 or x > TUK_WIDTH:
        x -= dirX * 10
    y += dirY * 5
    if y < 0 or y > TUK_HEIGHT:
        y -= dirY * 10

    delay(0.05)

close_canvas()

close_canvas()

