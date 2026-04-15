import sys
input = sys.stdin.readline

n, m = map(int, input().split())

maze = [list(map(int, input().split())) for _ in range(n)]

dp = [[0] * m for _ in range(n)]

dp[0][0] = maze[0][0]

for x in range(1, m):
    dp[0][x] = dp[0][x - 1] + maze[0][x]


for y in range(1, n):
    for x in range(m):
        if x == 0:
            dp[y][x] = dp[y - 1][x] + maze[y][x]
        else:
            dp[y][x] = max(dp[y-1][x], dp[y][x-1], dp[y-1][x-1]) + maze[y][x]
        
print(dp[-1][-1])