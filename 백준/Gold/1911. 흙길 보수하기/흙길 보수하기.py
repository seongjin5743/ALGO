import sys
input = sys.stdin.readline

n, l = map(int, input().split())

hole = [tuple(map(int, input().split())) for _ in range(n)]
hole.sort()

cnt = 0
cover = 0

for x, y in hole:
    start = max(cover, x)

    if start >= y:
        continue

    length = y - start
    need = (length + l - 1) // l

    cnt += need
    cover = start + need * l

print(cnt)