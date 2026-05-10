from collections import deque

for t in range(1, 11):
    n = int(input())
    maze = [list(map(int, input().strip())) for _ in range(100)]
    visited = [[False] * 100 for _ in range(100)]
    s_x, s_y, e_x, e_y = 0,0,0,0
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    for y in range(100):
        for x in range(100):
            if maze[y][x] == 2:
                s_x, s_y = x, y
            if maze[y][x] == 3:
                e_x, e_y = x, y

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
                if 0 <= nx < 100 and 0 <= ny < 100 and not visited[ny][nx]:
                    if maze[ny][nx] == 0 or maze[ny][nx] == 3:
                        queue.append((nx, ny))
                        visited[ny][nx] = True
        return 0
    answer = bfs(s_x, s_y)
    print(f"#{t} {answer}")