import pico2d
import math
import Map
import ClassPinn

pico2d.open_canvas(Map.WIDTH, Map.HEIGHT)

states = [ClassPinn]  # module을 변수로 취급
for state in states:
    state.enter()
    while state.running:
        state.handle_events()
        state.update()
        state.draw()
    state.exit()
# finalization code
pico2d.close_canvas()
