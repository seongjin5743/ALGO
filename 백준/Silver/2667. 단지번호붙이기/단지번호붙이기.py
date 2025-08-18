from collections import deque

n = int(input())

maze = []

for _ in range(n):
    ma = list(map(int, input()))
    maze.append(ma)

visited = [[False] * n for _ in range(n)]

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
    cnt = 1

    while queue:
        x, y= queue.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue

            if maze[nx][ny] == 0:
                continue

            if maze[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx,ny))
                cnt += 1


    return cnt

home = []

for i in range(n):
    for j in range(n):
        if not visited[i][j] and maze[i][j] == 1:
            home.append(bfs(i, j))

print(len(home))

home.sort()
for h in home:
    print(h)