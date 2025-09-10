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

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def solution():
    sx, sy = 0, 0

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
        sx, sy = sx + dx[dir], sy + dy[dir]

        if sx < 0 or sy < 0 or sx >= n or sy >= n or (sx, sy) in snake_set:
            return answer

        if maze[sx][sy] == 1:
            maze[sx][sy] = 0
            snake.append((sx, sy))
            snake_set.add((sx, sy))
        else:
            tail = snake.popleft()
            snake_set.remove(tail)
            snake.append((sx, sy))
            snake_set.add((sx, sy))

        if idx < l and answer == commands[idx][0]:
            _, ld = commands[idx]
            if ld == 'D':
                dir = (dir + 1) % 4
            else:
                dir = (dir - 1) % 4
            idx += 1

print(solution())