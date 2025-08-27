import sys
import bisect

input = sys.stdin.readline

n, m = map(int, input().split())

standard = []

for _ in range(n):
    x, y = input().split()
    standard.append((x, int(y)))

charactor = []
for _ in range(m):
    charactor.append(int(input()))

scores = [y for x, y in standard]

for c in charactor:
    idx = bisect.bisect_left(scores, c)
    print(standard[idx][0])