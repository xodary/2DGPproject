

mapping = [[0 for col in range(18)] for row in range(11)]

WIDTH, HEIGHT = 1200, 822
viewWIDTH, viewHEIGHT = 1200, 822
boxSizeW = 35
boxSizeH = 35

mapstartX = 229
mapstartY = 293

BIRTHEND, ENTRANCE, SUCCESS, FAIL, ARRIVAL, ORDER, NoDRINK, DRINK, BYE = range(9)

# event_table = {
#     BIRTH: {BIRTHEND, WALK},
#     WALK: {ENTRANCE: CHECK},
#     CHECK: {SUCCESS: IN, FAIL: REMOVE},
#     IN: {ARRIVAL: READY},
#     OUT: {ARRIVAL: REMOVE},    # OUT: 카페->입구, REMOVE: 입구 -> 삭제
#     READY: {ORDER: WAIT},
#     WAIT: {NoDRINK: BAD, DRINK: GOOD},
#     BAD: {BYE: OUT},
#     GOOD: {BYE: OUT}
# }



menuQueue = []
QueueTime = []
zombieSpawn = 100
EntranceX, EntranceY = 562, HEIGHT - 660

Looking = [[1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0], [-1, -1], [0, -1], [1, -1]]





