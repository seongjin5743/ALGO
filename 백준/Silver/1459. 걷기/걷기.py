import sys
input = sys.stdin.readline

x, y, w, s = map(int, input().split())

case1 = (x + y) * w

case2 = min(x, y) * s + abs(x - y) * w

if (x + y) % 2 == 0:
    case3 = max(x, y) * s
else:
    case3 = (max(x, y) - 1) * s + w

answer = min(case1, case2, case3)

print(answer)