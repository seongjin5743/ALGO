from collections import deque
import sys

input = sys.stdin.readline

t = int(input())

dx = [0,0,1,-1]
dy = [1,-1,0,0]

for _ in range(t):
    m, n, k = map(int, input().split())

    maze = [[0] * m for _ in range(n)]
    visited = [[False] * m for _ in range(n)]

    def bfs(x, y):
        queue = deque()
        queue.append((x, y))
        visited[y][x] = True

        while queue:
            x, y = queue.popleft()

            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]

                if 0 <= nx < m and 0 <= ny < n and not visited[ny][nx] and maze[ny][nx] == 1:
                    queue.append((nx, ny))
                    visited[ny][nx] = True
            
    for _ in range(k):
        x, y = map(int, input().split())

        maze[y][x] = 1
    
    sum = 0

    for y in range(n):
        for x in range(m):
            if maze[y][x] == 1 and not visited[y][x]:
                bfs(x, y)
                sum += 1
    print(sum)