from collections import deque

m, n, h = map(int, input().split())

maze = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]

queue = deque()

visited = [[[False] * m for _ in range(n)] for _ in range(h)]

for z in range(h):
    for y in range(n):
        for x in range(m):
            if maze[z][y][x] == 1:
                queue.append((x,y,z, 0))
                visited[z][y][x] = True

dx = [0,0,1,-1,0,0]
dy = [1,-1,0,0,0,0]
dz = [0,0,0,0,1,-1]

answer = -1

while queue:
    x,y,z, cnt = queue.popleft()

    answer = max(answer, cnt)

    for i in range(6):
        nx,ny,nz = x + dx[i], y + dy[i], z + dz[i]

        if 0 <= nx < m and 0 <= ny < n and 0 <= nz < h and not visited[nz][ny][nx]:
            if maze[nz][ny][nx] == 0:
                maze[nz][ny][nx] = 1
                queue.append((nx, ny, nz, cnt + 1))
                visited[nz][ny][nx] = True
                
if any(0 in row for layer in maze for row in layer):
    print(-1)
else:
    print(answer)