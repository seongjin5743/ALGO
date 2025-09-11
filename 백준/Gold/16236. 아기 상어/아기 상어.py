import sys 
from collections import deque

input = sys.stdin.readline

n = int(input())
maze = []
for _ in range(n):
    maze.append(list(map(int, input().split())))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
cnt = 0
x, y, size = 0, 0, 2

for i in range(n):
    for j in range(n):
        if maze[i][j] == 9:
            x = i
            y = j

def bfs(x,y,size):
    visited = [[False] * n for _ in range(n)]
    distance = [[0] * n for _ in range(n)]
    eat = []

    queue = deque()
    queue.append((x, y))
    visited[x][y] = True

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if maze[nx][ny] <= size:
                    queue.append((nx, ny))
                    visited[nx][ny] = True
                    distance[nx][ny] = distance[x][y] + 1
                    if maze[nx][ny] < size and maze[nx][ny] != 0:
                        eat.append((distance[nx][ny], nx, ny))
    return sorted(eat, key=lambda x : ((x[0], x[1], x[2])))

time = 0
count = 0
while True:
    shark = bfs(x,y,size)

    if not shark:
        break

    d, nx, ny = shark[0]
    time += d
    count += 1

    if size == count:
        size += 1
        count = 0

    maze[x][y] = 0
    x, y = nx, ny

print(time)