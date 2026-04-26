
from collections import deque



t = int(input())

for i in range(1, t + 1):
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
        
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            
            if 0 <= nx < n and 0 <= ny < n and not visited[ny][nx]:
                
                # 1. 그냥 이동
                if maze[y][x] > maze[ny][nx]:
                    visited[ny][nx] = True
                    dfs(nx, ny, length + 1, used)
                    visited[ny][nx] = False
                
                # 2. 깎아서 이동
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

    print(f'#{i} {answer}')