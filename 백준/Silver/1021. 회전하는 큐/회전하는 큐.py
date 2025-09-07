from collections import deque

n, m = map(int, input().split())
targets = list(map(int, input().split()))

dq = deque(range(1, n + 1))
count = 0

for t in targets:
    idx = dq.index(t)

    if idx <= len(dq) // 2:
        for _ in range(idx):
            dq.append(dq.popleft())
        count += idx
    else:
        for _ in range(len(dq) - idx):
            dq.appendleft(dq.pop())
        count += len(dq) - idx
    
    dq.popleft()

print(count)