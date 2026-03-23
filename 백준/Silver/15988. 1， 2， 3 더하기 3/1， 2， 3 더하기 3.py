t = int(input())

n = [int(input()) for _ in range(t)]

dp = [0] * (10000001)

dp[0] = 1
dp[1] = 1
dp[2] = 2

for i in range(3, 1000001):
    dp[i] = dp[i - 1] % 1000000009 + dp[i - 2] % 1000000009 + dp[i - 3] % 1000000009

for num in n:
    print(dp[num] % 1000000009)