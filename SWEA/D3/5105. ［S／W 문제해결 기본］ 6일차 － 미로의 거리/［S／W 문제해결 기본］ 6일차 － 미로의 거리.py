from collections import deque

T = int(input())

for t in range(1, T + 1):
    n = int(input())
    maze = [list(map(int, input().strip())) for _ in range(n)]
    visited = [[False] * n for _ in range(n)]
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    
    for y in range(n):
        for x in range(n):
            if maze[y][x] == 2:
                s_x, s_y = x, y
            if maze[y][x] == 3:
                e_x, e_y = x, y
    def bfs(x, y):
        queue = deque()
        queue.append((x, y, 0))
        visited[y][x] = True

        while queue:
            x, y, cnt = queue.popleft()

            if x == e_x and y == e_y:
                return cnt - 1
            
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < n and 0 <= ny < n and not visited[ny][nx]:
                    if maze[ny][nx] == 0 or maze[ny][nx] == 3:
                        queue.append((nx, ny, cnt + 1))
                        visited[ny][nx] = True
        return 0
    answer = bfs(s_x, s_y)
    print(f"#{t} {answer}")