from collections import deque

n, m = map(int, input().split())

maze = [[[] for _ in range(n)] for _ in range(n)]
room = [[0] * n for _ in range(n)]
visited = [[False] * n for _ in range(n)]

for _ in range(m):
    x, y, a, b = map(int, input().split())
    maze[y - 1][x - 1].append((a - 1, b - 1))

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visited[y][x] = True
    room[y][x] = 1
    cnt = 1
    
    while queue:
        x, y = queue.popleft()

        for a, b in maze[y][x]:
            if room[b][a] == 0:
                room[b][a] = 1
                cnt += 1

                for i in range(4):
                    nx, ny = a + dx[i], b + dy[i]
                    if 0 <= nx < n and 0 <= ny < n and visited[ny][nx]:
                        visited[b][a] = True
                        queue.append((a, b))
                        break

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[ny][nx]:
                if room[ny][nx] == 1:
                    visited[ny][nx] = True
                    queue.append((nx, ny))
    
    return cnt

print(bfs(0,0))