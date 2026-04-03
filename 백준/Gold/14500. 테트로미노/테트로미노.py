import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

visited = [[False] * m for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dfs(depth, temp, lst):
    global ans

    if depth == 4:
        ans = max(ans, temp)
        return

    for y, x in lst:
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < n and 0 <= nx < m and not visited[ny][nx]:
                visited[ny][nx] = True
                dfs(depth + 1, temp + arr[ny][nx], lst + [(ny, nx)])
                visited[ny][nx] = False

ans = 0

for y in range(n):
    for x in range(m):
        visited[y][x] = True
        dfs(1, arr[y][x], [(y, x)])

print(ans)