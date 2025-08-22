from collections import deque

n = int(input())

for _ in range(n):
    w, h = map(int, input().split())

    maze = [list(input().strip()) for _ in range(h)]
    visited = [[False] * w for _ in range(h)]
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]

    f_queue = deque()
    s_queue = deque()
    for y in range(h):
        for x in range(w):
            if maze[y][x] == '*':
                f_queue.append((x, y))
            elif maze[y][x] == '@':
                s_queue.append((x, y))
                visited[y][x] = True
    def bfs():

        count = 0
        while s_queue:
            count += 1

            for _ in range(len(f_queue)):
                x, y = f_queue.popleft()

                for i in range(4):
                    nx, ny = x + dx[i], y + dy[i]
                    
                    if 0 <= nx < w and 0 <= ny < h and maze[ny][nx] == '.':
                        maze[ny][nx] = '*'
                        f_queue.append((nx, ny))
            
            for _ in range(len(s_queue)):
                x, y = s_queue.popleft()

                if x == 0 or x == w - 1 or y == 0 or y == h - 1:
                    return count

                for i in range(4):
                    nx, ny = x + dx[i], y + dy[i]
                    
                    if 0 <= nx < w and 0 <= ny < h and not visited[ny][nx] and maze[ny][nx] == '.':
                        s_queue.append((nx, ny))
                        visited[ny][nx] = True
        return 'IMPOSSIBLE' 
    print(bfs())