from collections import deque

for t in range(1, 11):
    n, s = map(int, input().split())

    graph = [set() for _ in range(101)]
    visited = [False] * 101

    lst = list(map(int, input().split()))

    for i in range(0, len(lst), 2):
        graph[lst[i]].add(lst[i + 1])

    def bfs(x):
        queue = deque()
        queue.append(x)
        visited[x] = True

        answer = x

        while queue:
            size = len(queue)
            temp = []

            for _ in range(size):
                x = queue.popleft()

                for nx in graph[x]:
                    if not visited[nx]:
                        visited[nx] = True
                        queue.append(nx)
                        temp.append(nx)

            if temp:
                answer = max(temp)

        return answer

    print(f"#{t} {bfs(s)}")