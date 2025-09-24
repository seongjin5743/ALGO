from collections import deque

import sys

count = 0

while True:
    n = int(input())
    count += 1

    if n == 0:
        break

    maze = [list(map(int, input().split())) for _ in range(n)]

    dp = [[1e9] * n for _ in range(n)]
    
    dx = [0,0,-1,1]
    dy = [1,-1,0,0]

    def bfs(x, y):
        queue = deque()
        queue.append((x, y))
        dp[0][0] = maze[0][0]

        while queue:
            x, y = queue.popleft()

            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]

                if 0 <= nx < n and 0 <= ny < n:
                    if dp[y][x] + maze[ny][nx] < dp[ny][nx]:
                        dp[ny][nx] = dp[y][x] + maze[ny][nx]
                        queue.append((nx, ny))
        return dp[n -1][n - 1]
    
    print(f'Problem {count}: {bfs(0,0)}')