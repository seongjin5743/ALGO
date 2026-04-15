import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())

    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        x, y = map(int, input().split())
        graph[x].append(y)
        graph[y].append(x)

    visited = [False] * (n + 1)

    def dfs(x):
        visited[x] = True
        cnt = 0
        
        for nx in graph[x]:
            if not visited[nx]:
                cnt += 1 + dfs(nx)
        
        return cnt

    print(dfs(1))