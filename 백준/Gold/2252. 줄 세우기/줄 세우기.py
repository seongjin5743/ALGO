from collections import deque

n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]

indegree = [0] * (n + 1)

for _ in range(m):
   a, b = map(int, input().split())
   graph[a].append(b)
   indegree[b] += 1

def height():
    result = []

    queue = deque()
    for i in range(1, n + 1):
       if indegree[i] == 0:
          queue.append(i)

    while queue:
       x = queue.popleft()
       result.append(x)

       for g in graph[x]:
          indegree[g] -= 1
          if indegree[g] == 0:
             queue.append(g)
    print(*result)
   
height()