def get_dist(point1, point2):
    return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])


def dfs(r, c, dist, count):
    global res

    if dist >= res:
        return

    if count == N:
        res = min(res, dist + get_dist((r, c), home))
        return

    for i in range(N):
        if not visited[i]:
            visited[i] = True
            point = points[i]

            dfs(point[0], point[1],
                dist + get_dist((r, c), point),
                count + 1)

            visited[i] = False


T = int(input())

for test_case in range(1, T + 1):
    res = float('inf')

    N = int(input())
    temp = list(map(int, input().split()))

    company = (temp[0], temp[1])
    home = (temp[2], temp[3])

    points_list = temp[4:]
    points = []

    for i in range(0, len(points_list), 2):
        points.append((points_list[i], points_list[i + 1]))

    visited = [False] * N

    dfs(company[0], company[1], 0, 0)

    print(f"#{test_case} {res}")