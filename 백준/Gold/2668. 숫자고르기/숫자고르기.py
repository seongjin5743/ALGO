n = int(input())

graph = [[] for _ in range(n + 1)]
result = []

for i in range(1, n + 1):
    graph[i].append(int(input()))

def dfs(v, i):
    visited[v] = True

    for j in graph[v]:
        if not visited[j]:
            dfs(j, i)
        elif visited[j] and j == i:
            result.append(j)

for i in range(1, n + 1):
    visited = [False] * (n + 1)

    dfs(i, i)

print(len(result))
for r in result:
    print(r)