T = 10

for test_case in range(1, T + 1):
    N = int(input())
    lst = list(map(int, input().split()))

    for i in range(N):
        max_idx = lst.index(max(lst))
        min_idx = lst.index(min(lst))

        lst[max_idx] -= 1
        lst[min_idx] += 1

    print(f'#{test_case} {max(lst) - min(lst)}')