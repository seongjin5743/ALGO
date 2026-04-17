from collections import deque
import sys

input = sys.stdin.readline

n = int(input())

maze = list(map(int, input().split()))
visited = [False] * n

def bfs(x, cnt):
    queue = deque()
    queue.append((x, cnt))
    visited[x] = True

    while queue:
        x, cnt = queue.popleft()

        if x == n - 1:
            return cnt
        
        if maze[x] == 0:
            pass
        else:
            for i in range(x + 1, x + 1 + maze[x]):
                if 0 <= i < n and not visited[i]:
                    visited[i] = True
                    queue.append((i, cnt + 1))

    return -1

count = bfs(0, 0)

print(count)