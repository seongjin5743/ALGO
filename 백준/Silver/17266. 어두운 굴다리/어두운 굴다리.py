import math

n = int(input())
m = int(input())
x = list(map(int, input().split()))

h = max(x[0], n - x[-1])

for i in range(len(x) - 1):
    num = math.ceil((x[i + 1] - x[i]) / 2)
    h = max(num, h)

print(h)