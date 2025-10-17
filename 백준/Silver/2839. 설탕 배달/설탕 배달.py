import sys

input = sys.stdin.readline

n = int(input())

if n % 5 == 0:
    print(n // 5)
else:
    p = 0
    while n >= 0:
        if n % 5 == 0:
            print(p + n // 5)
            break
        n -= 3
        p += 1
    else:
        print(-1)