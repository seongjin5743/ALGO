from collections import deque

T = int(input())

for t in range(1, T + 1):
    V, E, n1, n2 = map(int, input().split())
    arr = list(map(int, input().split()))

    parent = [0] * (V + 1)
    tree = [[] for _ in range(V + 1)]

    for i in range(0, E * 2, 2):
        p = arr[i]
        c = arr[i + 1]

        parent[c] = p
        tree[p].append(c)

    visited = [False] * (V + 1)

    while n1:
        visited[n1] = True
        n1 = parent[n1]

    while n2:
        if visited[n2]:
            lca = n2
            break
        n2 = parent[n2]

    queue = deque([lca])
    count = 0

    while queue:
        now = queue.popleft()
        count += 1

        for nxt in tree[now]:
            queue.append(nxt)

    print(f"#{t} {lca} {count}")