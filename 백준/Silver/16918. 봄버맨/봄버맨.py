import sys
input = sys.stdin.readline

r, c, n = map(int, input().split())

maze1 = [input().strip() for _ in range(r)]

dx = [0,0,1,-1]
dy = [1,-1,0,0]

maze3 = [['O'] * c for _ in range(r)]

for y in range(r):
    for x in range(c):
        if maze1[y][x] == 'O':
            maze3[y][x] = '.'
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < c and 0 <= ny < r:
                    maze3[ny][nx] = '.'

maze5 = [['O'] * c for _ in range(r)]

for y in range(r):
    for x in range(c):
        if maze3[y][x] == 'O':
            maze5[y][x] = '.'
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < c and 0 <= ny < r:
                    maze5[ny][nx] = '.'

if n == 1:
    answer = maze1
elif n % 2 == 0:
    answer = [['O'] * c for _ in range(r)]
elif n % 4 == 3:
    answer = maze3
else:
    answer = maze5

for row in answer:
    print(''.join(row))