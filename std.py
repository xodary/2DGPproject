
# 16 x 11 xy
# mapping = [[0 for col in range(100)] for row in range(100)]





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
# EntranceX, EntranceY = 562, gamePlay.viewHEIGHT - 660







