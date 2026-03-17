import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

maze_t = [list(input().strip()) for _ in range(n)]
visited_t = [[False] * n for _ in range(n)]

maze_j = [row[:] for row in maze_t]
visited_j = [[False] * n for _ in range(n)]
for y in range(n):
    for x in range(n):
        if maze_j[y][x] == 'G':
            maze_j[y][x] = 'R'

dx = [0,0,-1,1]
dy = [1,-1,0,0]

def bfs_t(x, y, color):
    queue = deque()
    visited_t[y][x] = True
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and not visited_t[ny][nx] and maze_t[ny][nx] == color:
                queue.append((nx, ny))
                visited_t[ny][nx] = True

def bfs_j(x, y, color):
    queue = deque()
    visited_j[y][x] = True
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and not visited_j[ny][nx] and maze_j[ny][nx] == color:
                queue.append((nx, ny))
                visited_j[ny][nx] = True

sum_t, sum_j = 0, 0

for y in range(n):
    for x in range(n):
        if not visited_t[y][x]:
            bfs_t(x, y, maze_t[y][x])
            sum_t += 1
        if not visited_j[y][x]:
            bfs_j(x, y, maze_j[y][x])
            sum_j += 1

print(sum_t, sum_j)