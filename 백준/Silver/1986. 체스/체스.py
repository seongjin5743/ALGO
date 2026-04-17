import sys
input = sys.stdin.readline

n, m = map(int, input().split())

maze = [[0] * m for _ in range(n)]

q = list(map(int, input().split()))
k = list(map(int, input().split()))
p = list(map(int, input().split()))

queen = []
knight = []

if q[0] != 0:
    for i in range(q[0]):
        y = q[2*i + 1] - 1
        x = q[2*i + 2] - 1
        queen.append((y, x))
        maze[y][x] = 1

if k[0] != 0:
    for i in range(k[0]):
        y = k[2*i + 1] - 1
        x = k[2*i + 2] - 1
        knight.append((y, x))
        maze[y][x] = 1

if p[0] != 0:
    for i in range(p[0]):
        y = p[2*i + 1] - 1
        x = p[2*i + 2] - 1
        maze[y][x] = 1

dy = [1,1,1,0,0,-1,-1,-1]
dx = [1,0,-1,1,-1,1,0,-1]

for y, x in queen:
    for d in range(8):
        ny, nx = y, x

        while True:
            ny += dy[d]
            nx += dx[d]

            if ny < 0 or nx < 0 or ny >= n or nx >= m:
                break

            if maze[ny][nx] == 1:
                break

            if maze[ny][nx] == 0:
                maze[ny][nx] = -1

kdy = [2,2,1,1,-1,-1,-2,-2]
kdx = [1,-1,2,-2,2,-2,1,-1]

for y, x in knight:
    for d in range(8):
        ny = y + kdy[d]
        nx = x + kdx[d]

        if 0 <= ny < n and 0 <= nx < m:
            if maze[ny][nx] == 0:
                maze[ny][nx] = -1

count = 0
for i in range(n):
    for j in range(m):
        if maze[i][j] == 0:
            count += 1

print(count)