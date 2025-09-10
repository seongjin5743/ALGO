import sys
input = sys.stdin.readline

n = int(input())
dots = set()

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

for _ in range(n):
    x,y,d,g = map(int, input().split())

    directions = [d]
    for _ in range(g):
        directions += [(dir + 1) % 4 for dir in directions[::-1]]
    
    dots.add((x, y))

    for dir in directions:
        x, y = x + dx[dir], y + dy[dir]
        dots.add((x, y))

ans = 0
for i in range(100):
    for j in range(100):
        if (i, j) in dots and (i+1, j) in dots and (i, j+1) in dots and (i+1, j+1) in dots:
            ans += 1

print(ans)