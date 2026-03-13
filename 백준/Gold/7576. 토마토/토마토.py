import sys
from collections import deque

input = sys.stdin.readline

m, n = map(int, input().split())

maze = [list(map(int, input().split())) for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

queue = deque()

for y in range(n):
    for x in range(m):
        if maze[y][x] == 1:
            queue.append((x, y))

while queue:
    x, y = queue.popleft()

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if 0 <= nx < m and 0 <= ny < n and maze[ny][nx] == 0:
            queue.append((nx, ny))
            maze[ny][nx] = maze[y][x] + 1

answer = 0

for row in maze:
    if 0 in row:
        print(-1)
        break
    answer = max(answer, max(row))
else:
    print(answer - 1)