t = int(input())

dp = [[0] * 10001 for _ in range(4)]
dp[0][0] = 1

for i in range(1, 4):
    for j in range(10001):
        dp[i][j] = dp[i - 1][j]

        if j >= i:
            dp[i][j] += dp[i][j - i]
for _ in range(t):
    num = int(input())
    print(dp[3][num])