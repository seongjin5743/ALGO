from collections import deque

T = int(input())

for t in range(1, T + 1):
    n, k = map(int, input().split())
    maze = [list(map(int, input().split())) for _ in range(n)]

    top = max(map(max, maze))
    result = []

    for y in range(n):
        for x in range(n):
            if maze[y][x] == top:
                result.append((x, y))

    dx = [0,0,-1,1]
    dy = [1,-1,0,0]

    def dfs(x, y, length, used):
        global answer
        answer = max(answer, length)

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < n and not visited[ny][nx]:
                if maze[ny][nx] < maze[y][x]:
                    visited[ny][nx] = True
                    dfs(nx, ny, length + 1, used)
                    visited[ny][nx] = False
                elif not used and maze[ny][nx] - k < maze[y][x]:
                    original = maze[ny][nx]
                    maze[ny][nx] = maze[y][x] - 1
                    visited[ny][nx] = True
                    dfs(nx, ny, length + 1, True)
                    visited[ny][nx] = False
                    maze[ny][nx] = original
    answer = 0
    for x, y in result:
        visited = [[False] * n for _ in range(n)]
        visited[y][x] = True
        dfs(x, y, 1, False)

    print(f'#{t} {answer}')