import sys
from collections import deque

input = sys.stdin.readline

n, m, p = map(int, input().split())
s = list(map(int, input().split()))
board = [list(input().strip()) for _ in range(n)]

queues = [deque() for _ in range(p + 1)]

for i in range(n):
    for j in range(m):
        if board[i][j].isdigit():
            player = int(board[i][j])
            queues[player].append((i, j))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

while True:
    moved = False
    for player in range(1, p + 1):
        step = s[player - 1]
        q = queues[player]

        for _ in range(step):
            size = len(q)
            if size == 0:
                break
            for _ in range(size):
                x, y = q.popleft()
                for k in range(4):
                    nx, ny = x + dx[k], y + dy[k]
                    if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == '.':
                        board[nx][ny] = str(player)
                        q.append((nx, ny))
                        moved = True
    if not moved:
        break

answer = [0] * (p + 1)
for i in range(n):
    for j in range(m):
        if board[i][j].isdigit():
            answer[int(board[i][j])] += 1

print(*answer[1:])
