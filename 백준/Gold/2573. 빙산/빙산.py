from collections import deque

n, m = map(int, input().split())
maze = [list(map(int, input().split())) for _ in range(n)]

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

def bfs(sy, sx, visited):
    queue = deque([(sy, sx)])
    visited[sy][sx] = True
    while queue:
        y, x = queue.popleft()
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < n and 0 <= nx < m:
                if maze[ny][nx] > 0 and not visited[ny][nx]:
                    visited[ny][nx] = True
                    queue.append((ny, nx))

def melt():
    changes = []
    for y in range(n):
        for x in range(m):
            if maze[y][x] > 0:
                sea_count = 0
                for i in range(4):
                    ny, nx = y + dy[i], x + dx[i]
                    if 0 <= ny < n and 0 <= nx < m and maze[ny][nx] == 0:
                        sea_count += 1
                if sea_count > 0:
                    changes.append((y, x, sea_count))

    for y, x, c in changes:
        maze[y][x] = max(0, maze[y][x] - c)

answer = 0
while True:
    visited = [[False] * m for _ in range(n)]
    count = 0

    for y in range(n):
        for x in range(m):
            if maze[y][x] > 0 and not visited[y][x]:
                bfs(y, x, visited)
                count += 1

    if count == 0:
        answer = 0
        break
    if count >= 2:
        break

    melt()
    answer += 1

print(answer)
