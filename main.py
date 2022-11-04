import pico2d
import gamePlay
import std

pico2d.open_canvas(std.WIDTH, std.HEIGHT)

states = [gamePlay]  # module을 변수로 취급
for state in states:
    state.enter()
    while state.running:
        state.handle_events()
        state.update()
        state.draw()
    state.exit()
# finalization code
pico2d.close_canvas()
