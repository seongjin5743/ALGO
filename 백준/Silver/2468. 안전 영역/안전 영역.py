n = int(input())

maze = []

for _ in range(n):
    ma = list(map(int, input().split()))
    maze.append(ma)

visited = [[False] * n for _ in range(n)]

from collections import deque

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs(x, y, cnt):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue

            if not visited[nx][ny] and maze[nx][ny] > cnt:
                visited[nx][ny] = True
                queue.append((nx, ny))

count = 0
for c in range(max(map(max, maze))):
    cnt = 0
    for i in range(n):
        for j in range(n):
            if not visited[i][j] and maze[i][j] > c:
                bfs(i, j, c)
                cnt += 1
    count = max(count, cnt)
    visited = [[False] * n for _ in range(n)]

print(count)