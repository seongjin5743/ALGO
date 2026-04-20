from collections import deque
import sys

input = sys.stdin.readline

r, c = map(int, input().split())
maze = [list(input().strip()) for _ in range(r)]

visited = [[False] * c for _ in range(r)]

dx = [0,0,-1,1]
dy = [1,-1,0,0]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visited[y][x] = True

    wolf, sheep = 0, 0
    if maze[y][x] == 'o':
        sheep += 1
    elif maze[y][x] == 'v':
        wolf += 1

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < c and 0 <= ny < r:
                if not visited[ny][nx] and maze[ny][nx] != '#':
                    visited[ny][nx] = True

                    if maze[ny][nx] == 'o':
                        sheep += 1
                    elif maze[ny][nx] == 'v':
                        wolf += 1

                    queue.append((nx, ny))

    if sheep > wolf:
        return 0, sheep
    else:
        return wolf, 0


total_wolf = 0
total_sheep = 0

for y in range(r):
    for x in range(c):
        if not visited[y][x] and maze[y][x] != '#':
            wolf, sheep = bfs(x, y)
            total_wolf += wolf
            total_sheep += sheep

print(total_sheep, total_wolf)