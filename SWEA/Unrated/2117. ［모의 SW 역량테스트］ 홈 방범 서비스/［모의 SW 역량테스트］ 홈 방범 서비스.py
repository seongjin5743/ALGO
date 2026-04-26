T = int(input())

for t in range(1, T + 1):
    n, m = map(int, input().split())
    maze = [list(map(int, input().split())) for _ in range(n)]

    answer = 0

    for k in range(1, n + 2):
        cost = k * k + (k - 1) * (k - 1)

        for x in range(n):
            for y in range(n):
                cnt = 0
                
                for i in range(n):
                    for j in range(n):
                        if abs(x - i) + abs(y - j) < k:
                            cnt += maze[i][j]

                # 수익 계산
                if cnt * m >= cost:
                    answer = max(answer, cnt)

    print(f"#{t} {answer}")