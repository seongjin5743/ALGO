import sys

input = sys.stdin.readline

m = int(input())

for _ in range(m):
    t = int(input())
    n = 2
    while t > 1:
        count = 0
        while t % n == 0:
            count += 1
            t //= n
        if count > 0:
            print(n, count)
        n += 1