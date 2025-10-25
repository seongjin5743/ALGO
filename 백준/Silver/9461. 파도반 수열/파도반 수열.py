n = int(input())

for _ in range(n):
    m = int(input())

    dp = [0,1,1,1] + [0] * (m - 3)
    
    for i in range(4, m + 1):
        dp[i] = dp[i - 2] + dp[i - 3]
    print(dp[m])