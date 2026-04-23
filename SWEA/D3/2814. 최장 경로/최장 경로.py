t = int(input())

for i in range(1, t + 1):
    n, m = map(int, input().split())

    graph = [[] for _ in range(n + 1)]

    for _ in range(m):
        x, y = map(int, input().split())
        graph[x].append(y)
        graph[y].append(x)

    count = 1

    def dfs(node, cnt):
        global count
        count = max(count, cnt)

        for next_node in graph[node]:
            if not visited[next_node]:
                visited[next_node] = True
                dfs(next_node, cnt + 1)
                visited[next_node] = False

    for start in range(1, n + 1):
        visited = [False] * (n + 1)
        visited[start] = True
        dfs(start, 1)

    print(f'#{i} {count}')