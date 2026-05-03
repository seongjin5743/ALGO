T = int(input())

for t in range(1, T + 1):
    n = int(input())

    A = [int(input()) for _ in range(n)]

    dp = [0] * n
    dp[0] = A[0]
    for i in range(1, n):
        dp[i] = max(A[i], dp[i - 1] + A[i])

    print(f"#{t} {max(dp)}")