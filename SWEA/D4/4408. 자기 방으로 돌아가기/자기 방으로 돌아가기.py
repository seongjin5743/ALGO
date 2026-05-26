T = int(input())

for t in range(1, T + 1):
    n = int(input())
    corridor = [0] * 201

    for _ in range(n):
        start, end = map(int, input().split())

        s = (start + 1) // 2
        e = (end + 1) // 2

        if s > e:
            s, e = e, s

        for i in range(s, e + 1):
            corridor[i] += 1

    answer = max(corridor)

    print(f"#{t} {answer}")