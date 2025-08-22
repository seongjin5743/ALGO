n = int(input())

maze = [list(map(int, input().split())) for _ in range(n)]

dp = [[0] * i for i in range(1, n + 1)]
dp[0][0] = maze[0][0]

for i in range(1, len(maze)):
    for j in range(i + 1):
        if j == 0:
            dp[i][j] = dp[i - 1][j] + maze[i][j]
        elif j == i:
            dp[i][j] = dp[i - 1][j - 1] + maze[i][j]
        else:
            dp[i][j] = maze[i][j] + max(dp[i - 1][j], dp[i - 1][j - 1])
print(max(dp[n - 1]))