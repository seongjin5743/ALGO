T = int(input())

for t in range(1, T + 1):
    arr = list(map(int, input().split()))

    S = sum(arr)
    M = max(arr)

    for x in range(M + 1, M + 8):
        if (S + x) % 7 == 0:
            print(x)
            break