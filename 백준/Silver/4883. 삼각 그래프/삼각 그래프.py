num = 1

while True:
    n = int(input())

    if n == 0:
        break
    
    maze = [list(map(int, input().split())) for _ in range(n)]

    dp = [[0] * 3 for _ in range(n)]

    dp[0][1] = maze[0][1]
    dp[0][2] = dp[0][1] + maze[0][2]
    dp[1][0] = dp[0][1] + maze[1][0]
    dp[1][1] = min(dp[0][1], dp[0][2], dp[1][0]) + maze[1][1]
    dp[1][2] = min(dp[0][1], dp[0][2], dp[1][1]) + maze[1][2]

    for i in range(2, n):
        dp[i][0] = min(dp[i-1][0], dp[i-1][1]) + maze[i][0]
        dp[i][1] = min(dp[i-1][0], dp[i-1][1], dp[i-1][2], dp[i][0]) + maze[i][1]
        dp[i][2] = min(dp[i-1][1], dp[i-1][2], dp[i][1]) + maze[i][2]
    
    print('%d. %d' % (num, dp[-1][1]))
    num += 1