from collections import deque
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
maze = [list(input().strip()) for _ in range(n)]

dx = [0,0,-1,1]
dy = [1,-1,0,0]

def bfs(x, y):
    visited = [[False] * m for _ in range(n)]
    
    queue = deque()
    queue.append((x, y, 0))
    visited[y][x] = True
    
    max_dist = 0

    while queue:
        x, y, dist = queue.popleft()
        max_dist = max(max_dist, dist)

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < m and 0 <= ny < n:
                if not visited[ny][nx] and maze[ny][nx] == 'L':
                    visited[ny][nx] = True
                    queue.append((nx, ny, dist + 1))

    return max_dist

dist = 0
for y in range(n):
    for x in range(m):
        if maze[y][x] == 'L':
            dist = max(dist, bfs(x, y))
print(dist)