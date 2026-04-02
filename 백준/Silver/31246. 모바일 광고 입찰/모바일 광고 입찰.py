import sys

input = sys.stdin.readline

n, k = map(int, input().split())

moloco = []

for _ in range(n):
    a, b = map(int, input().split())
    moloco.append((a, b))

moloco.sort(key=lambda x: x[0] - x[1], reverse=True)

if moloco[k - 1][0] - moloco[k - 1][1] < 0:
    print(moloco[k - 1][1] - moloco[k - 1][0])
else:
    print(0)