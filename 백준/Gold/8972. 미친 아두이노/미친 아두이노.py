import sys
input = sys.stdin.readline

def robot_moving(me, robot):
    r, c = 0, 0

    if me[0] > robot[0]:
        r = 1
    elif me[0] < robot[0]:
        r = -1

    if me[1] > robot[1]:
        c = 1
    elif me[1] < robot[1]:
        c = -1

    return r, c


r, c = map(int, input().split())
maze = [list(input().strip()) for _ in range(r)]
commands = list(map(int, input().strip()))

Ix, Iy = 0, 0
arduinos = set()

for y in range(r):
    for x in range(c):
        if maze[y][x] == 'I':
            Iy, Ix = y, x
        elif maze[y][x] == 'R':
            arduinos.add((y, x))


for turn, command in enumerate(commands, 1):

    dr = [0,1,1,1,0,0,0,-1,-1,-1]
    dc = [0,-1,0,1,-1,0,1,-1,0,1]

    Iy += dr[command]
    Ix += dc[command]

    if (Iy, Ix) in arduinos:
        print(f'kraj {turn}')
        exit()

    next_robots = set()
    boom = set()

    for ry, rx in arduinos:
        dy, dx = robot_moving((Iy, Ix), (ry, rx))

        ny = ry + dy
        nx = rx + dx

        if (ny, nx) == (Iy, Ix):
            print(f'kraj {turn}')
            exit()

        if (ny, nx) in next_robots:
            boom.add((ny, nx))
        else:
            next_robots.add((ny, nx))

    arduinos = next_robots - boom


board = [['.'] * c for _ in range(r)]
board[Iy][Ix] = 'I'

for y, x in arduinos:
    board[y][x] = 'R'

for row in board:
    print(''.join(row))