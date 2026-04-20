from collections import deque
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
maze = [list(map(int, input().split())) for _ in range(m)]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

visited = [[False] * n for _ in range(m)]
room_id = [[0] * n for _ in range(m)]
room_size = []

def bfs(x, y, idx):
    queue = deque()
    queue.append((x, y))
    visited[y][x] = True
    room_id[y][x] = idx
    cnt = 1

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            if not (maze[y][x] & (1 << i)):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < n and 0 <= ny < m and not visited[ny][nx]:
                    visited[ny][nx] = True
                    room_id[ny][nx] = idx
                    queue.append((nx, ny))
                    cnt += 1

    return cnt

idx = 0
for y in range(m):
    for x in range(n):
        if not visited[y][x]:
            room_size.append(bfs(x, y, idx))
            idx += 1

max_room = 0

for y in range(m):
    for x in range(n):
        for i in range(4):
            if maze[y][x] & (1 << i):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < n and 0 <= ny < m:
                    a = room_id[y][x]
                    b = room_id[ny][nx]

                    if a != b:
                        max_room = max(max_room, room_size[a] + room_size[b])

print(idx)
print(max(room_size))
print(max_room)