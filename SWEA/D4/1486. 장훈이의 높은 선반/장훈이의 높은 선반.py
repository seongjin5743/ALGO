T = int(input())

for t in range(1, T + 1):
    N, B = map(int, input().split())
    arr = list(map(int, input().split()))

    answer = float('inf')

    def dfs(idx, total):
        global answer

        if total >= B:
            answer = min(answer, total)
            return

        if idx == N:
            return 

        dfs(idx + 1, total + arr[idx])

        dfs(idx + 1, total)

    dfs(0, 0)

    print(f'#{t} {answer - B}')