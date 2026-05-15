def dfs(x):
    global answer

    if x == M:
        answer = max(answer, int(''.join(arr)))
        return

    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            arr[i], arr[j] = arr[j], arr[i]

            check = int(''.join(arr))
            if (x, check) not in visited:
                visited.append((x, check))
                dfs(x + 1)

            arr[i], arr[j] = arr[j], arr[i]

T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())
    arr = list(str(N))
    visited = []
    answer = 0
    dfs(0)
    print(f'#{t} {answer}')