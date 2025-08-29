n, m = map(int, input().split())

maze = []

for _ in range(n):
    ma = list(map(int, input().split()))
    maze.append(ma)

visited = [[False] * m for _ in range(n)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
from collections import deque

a_x, a_y = 0, 0

for y in range(n):
    for x in range(m):
        if maze[y][x] == 2:
            a_x, a_y = x, y
            maze[y][x] = 0
            break

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visited[y][x] = True

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < m and 0 <= ny < n and not visited[ny][nx] and maze[ny][nx] == 1:
                maze[ny][nx] = maze[y][x] + 1
                visited[ny][nx] = True
                queue.append((nx, ny))         

bfs(a_x, a_y)

for y in range(n):
    for x in range(m):
        if maze[y][x] == 1 and not visited[y][x]:
            maze[y][x] = -1

for i in range(n):
    print(*maze[i])