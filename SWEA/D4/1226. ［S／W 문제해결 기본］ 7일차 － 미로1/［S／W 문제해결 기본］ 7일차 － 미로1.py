from collections import deque

for _ in range(10):
    t = int(input())
    maze = [list(map(int, input().strip())) for _ in range(16)]

    s_x, s_y = 0, 0
    e_x, e_y = 0, 0

    for y in range(16):
        for x in range(16):
            if maze[y][x] == 2:
                s_x, s_y = x, y
            if maze[y][x] == 3:
                e_x, e_y = x, y
    
    visited = [[False] * 16 for _ in range(16)]
    
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    
    def bfs(x, y):
        queue = deque()
        queue.append((x, y))
        visited[y][x] = True

        while queue:
            x, y = queue.popleft()
            
            if x == e_x and y == e_y:
                return 1
            
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]

                if 0 <= nx < 16 and 0 <= ny < 16 and not visited[ny][nx] and (maze[ny][nx] == 0 or maze[ny][nx] == 3):
                    queue.append((nx, ny))
                    visited[ny][nx] = True
        return 0
    print(f'#{t} {bfs(s_x, s_y)}')