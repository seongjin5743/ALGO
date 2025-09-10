from collections import deque
import sys

input = sys.stdin.readline

n = int(input())
k = int(input())

maze = [[0] * n for _ in range(n)]

for _ in range(k):
    y, x = map(int, input().split())
    maze[y-1][x-1] = 1

l = int(input())

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

def solution():
    sy, sx = 0, 0

    snake = deque([(0, 0)])
    snake_set = set([(0, 0)])
    dir = 0
    
    answer = 0

    commands = []
    for _ in range(l):
        sec, ld = input().split()
        commands.append((int(sec), ld))

    idx = 0
    while True:
        answer += 1
        sy, sx = sy + dy[dir], sx + dx[dir]

        if sy < 0 or sx < 0 or sy >= n or sx >= n or (sy, sx) in snake_set:
            return answer

        if maze[sy][sx] == 1:
            maze[sy][sx] = 0
            snake.append((sy, sx))
            snake_set.add((sy, sx))
        else:
            tail = snake.popleft()
            snake_set.remove(tail)
            snake.append((sy, sx))
            snake_set.add((sy, sx))

        if idx < l and answer == commands[idx][0]:
            _, ld = commands[idx]
            if ld == 'D':
                dir = (dir + 1) % 4
            else:
                dir = (dir - 1) % 4
            idx += 1

print(solution())