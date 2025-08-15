from collections import deque

nums = [i for i in range(1, int(input()) + 1)]

queue = deque(nums)

while len(queue) != 1:
    queue.popleft()
    queue.append(queue.popleft())


print(*queue)