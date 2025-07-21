N = int(input())

for _ in range(N):
    x, y = input().split()

    x = list(x)
    y = list(y)
    x.sort()
    y.sort()
    if x == y:
        print("Possible")
    else:
        print('Impossible')