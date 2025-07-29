n, m = map(int, input().split())

maze = []
for _ in range(n):
    ma = list(map(int, input()))
    maze.append(ma)

from collections import deque

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            
            if maze[nx][ny] == 0:
                continue
            
            if maze[nx][ny] == 1:
                maze[nx][ny] = maze[x][y] + 1
                queue.append((nx, ny))
    return maze[-1][-1]


print(bfs(0,0))