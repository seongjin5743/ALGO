from collections import deque
import sys

input = sys.stdin.readline

while True:
    w, h = map(int, input().split())

    if w == 0 and h == 0:
        break

    maze = [list(map(int, input().split())) for _ in range(h)]
    
    dx = [1,1,1,0,0,-1,-1,-1]
    dy = [1,0,-1,1,-1,1,0,-1]

    if w == h == 1:
        if maze[0][0] == 1:
            print(1)
        else:
            print(0)
    else:
        count = 0
        visited = [[False] * w for _ in range(h)]

        def bfs(x, y):
            queue = deque()
            queue.append((x, y))
            visited[y][x] = True

            while queue:
                x, y = queue.popleft()
                for i in range(8):
                    nx, ny = x + dx[i], y + dy[i]
                    if 0 <= nx < w and 0 <= ny < h and not visited[ny][nx] and maze[ny][nx] == 1:
                        visited[ny][nx] = True
                        queue.append((nx, ny))

        for y in range(h):
            for x in range(w):
                if not visited[y][x] and maze[y][x] == 1:
                    bfs(x, y)
                    count += 1
        print(count)