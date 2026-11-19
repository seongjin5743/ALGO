T = 10
for test_case in range(1, T + 1):
    N = int(input())
    lst = list(map(int, input().split()))
    lst.sort()
    for i in range(N):
        lst[0] += 1
        lst[-1] -= 1
        lst.sort()
    print(f'#{test_case} {lst[-1] - lst[0]}')