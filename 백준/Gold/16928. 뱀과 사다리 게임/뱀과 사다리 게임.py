from collections import deque

n, m = map(int, input().split())

graph = list(range(101))
for _ in range(n + m):
    a, b = map(int, input().split())
    graph[a] = b

def bfs(v):
    queue = deque([v])
    visited[v] = 0

    while queue:
        target = queue.popleft()

        for i in range(1, 7):
            dice = target + i
            if dice > 100:
                continue

            cnt = graph[dice]

            if visited[cnt] == -1:
                visited[cnt] = visited[target] + 1
                queue.append(cnt)

                if cnt == 100:
                    return

visited = [-1] * 101
bfs(1)

print(visited[100])