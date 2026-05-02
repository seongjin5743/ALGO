T = int(input())

for t in range(1, T + 1):
    n, l = map(int, input().split())
    food = [tuple(map(int, input().split())) for _ in range(n)]
    
    dp = [0] * (l + 1)
    
    for score, cal in food:
        for i in range(l, cal - 1, -1):
            dp[i] = max(dp[i], dp[i - cal] + score)
    
    print(f'#{t} {max(dp)}')