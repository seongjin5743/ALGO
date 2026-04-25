from itertools import combinations

t = int(input())

for i in range(1, t + 1):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    a.sort()

    answer = 1e9

    for j in range(n - k + 1):
        answer = min(answer, a[j + k - 1] - a[j])

    print(f'#{i} {answer}')