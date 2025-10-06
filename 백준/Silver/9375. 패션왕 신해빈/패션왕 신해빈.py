n = int(input())
for _ in range(n):
    m = int(input())
    f = {}
    for _ in range(m):
        item, gear = input().split()
        if gear not in f:
            f[gear] = 1
        else:
            f[gear] += 1
    result = 1
    for count in f.values():
        result *= (count + 1)
    print(result - 1)