import sys

input = sys.stdin.readline

n = int(input())

s_x, s_y, e_x, e_y = map(int, input().split())

dis = []

def distance(x, y, x1, y1):
    return abs(x - x1) + abs(y - y1)

for _ in range(n):
    x = int(input())
    
    dots = [(s_x, s_y)]
    for _ in range(x):
        nx, ny = map(int, input().split())
        dots.append((nx, ny))
    dots.append((e_x, e_y))
    
    answer = 0
    for i in range(0, len(dots) - 1):
        answer += distance(dots[i][0], dots[i][1], dots[i + 1][0], dots[i + 1][1])
    dis.append(answer)

print(dis.index(min(dis)) + 1)
