import sys
from collections import deque
input = sys.stdin.readline

n, s = map(int, input().split())
s -= 1

x = list(map(int, input().split()))
h = list(map(int, input().split()))

visited = [False] * n
q = deque([s])
visited[s] = True

left = right = s
min_pos = x[s]
max_pos = x[s]

while q:
    cur = q.popleft()

    min_pos = min(min_pos, x[cur] - h[cur])
    max_pos = max(max_pos, x[cur] + h[cur])

    while left - 1 >= 0 and x[left - 1] >= min_pos:
        left -= 1
        if not visited[left]:
            visited[left] = True
            q.append(left)

    while right + 1 < n and x[right + 1] <= max_pos:
        right += 1
        if not visited[right]:
            visited[right] = True
            q.append(right)

for i in range(left, right + 1):
    print(i + 1, end=" ")