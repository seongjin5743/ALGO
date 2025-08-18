from collections import deque

r, c = map(int, input().split())
maze = [list(input().strip()) for _ in range(r)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

f_q = deque()
j_q = deque()
visited = [[False] * c for _ in range(r)]

for y in range(r):
    for x in range(c):
        if maze[y][x] == 'F':
            f_q.append((x, y))
        elif maze[y][x] == 'J':
            j_q.append((x, y))
            visited[y][x] = True

def bfs():
    time = 0
    while j_q:
        time += 1

        for _ in range(len(f_q)):
            x, y = f_q.popleft()
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < c and 0 <= ny < r and maze[ny][nx] == '.':
                    maze[ny][nx] = 'F'
                    f_q.append((nx, ny))

        for _ in range(len(j_q)):
            x, y = j_q.popleft()

            if x == 0 or x == c - 1 or y == 0 or y == r - 1:
                return time

            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < c and 0 <= ny < r and not visited[ny][nx] and maze[ny][nx] == '.':
                    visited[ny][nx] = True
                    j_q.append((nx, ny))

    return "IMPOSSIBLE"

print(bfs())