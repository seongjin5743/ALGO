import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

maze = [list(map(int, input().strip())) for _ in range(n)]

visited = [[False] * m for _ in range(n)]

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs(x, y):
    queue = deque()
    queue.append((x, y, 1))
    visited[y][x] = True

    while queue:
        x, y, cnt = queue.popleft()

        if x == m - 1 and y == n - 1:
            return cnt

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < m and 0 <= ny < n and not visited[ny][nx] and maze[ny][nx] == 1:
                visited[ny][nx] = True
                queue.append((nx, ny, cnt + 1))

print(bfs(0, 0))