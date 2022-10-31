from collections import deque
from std import *

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(xPos, yPos, tableX, tableY, path):
    queue = deque()
    queue.append((xPos, yPos))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if nx < 0 or ny < 0 or nx >= tableX or ny >= tableY:
                continue

            if mapping[nx][ny] == 0:
                continue

            if mapping[nx][ny] == 1:
                path[nx][ny] = mapping[x][y] + 1

                queue.append((nx, ny))

    return path