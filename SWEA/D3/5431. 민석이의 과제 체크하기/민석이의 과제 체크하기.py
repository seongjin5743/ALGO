t = int(input())

for i in range(1, t + 1):
    n, k = map(int, input().split())

    n_lst = list(map(int, input().split()))

    answer = []
    for num in range(1, n + 1):
        if num not in n_lst:
            answer.append(num)

    print(f'#{i} ', end='')
    print(*answer)