T = int(input())

for t in range(1, T + 1):
    n = int(input())
    place = list(map(int, input().split()))

    s_x, s_y = place[:2]
    e_x, e_y = place[2:4]

    xy = []
    for i in range(4, len(place), 2):
        x, y = place[i:i+2]
        xy.append((x, y))

    visited = [False] * n
    answer = float('inf')

    def dfs(x, y, dist, cnt):
        global answer

        if dist >= answer:
            return

        if cnt == n:
            dist += abs(x - e_x) + abs(y - e_y)
            answer = min(answer, dist)
            return

        for i in range(n):
            if not visited[i]:
                nx, ny = xy[i]
                visited[i] = True

                d = abs(x - nx) + abs(y - ny)
                dfs(nx, ny, dist + d, cnt + 1)

                visited[i] = False

    dfs(s_x, s_y, 0, 0)

    print(f"#{t} {answer}")