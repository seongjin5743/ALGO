T = int(input())

for t in range(1, T + 1):
    x, y = map(int, input().split())

    a = (x + y) // 2
    b = x - a
    print(a, b)