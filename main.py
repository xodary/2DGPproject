import game_framework
import pico2d

import gamePlay

pico2d.open_canvas(1920, 1280)
game_framework.run(gamePlay)
pico2d.close_canvas()