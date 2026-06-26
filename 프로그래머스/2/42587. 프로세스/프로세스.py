import heapq
from collections import deque

def solution(priorities, location):
    queue = deque()
    heap = []

    for idx, num in enumerate(priorities):
        queue.append((idx, num))
        heapq.heappush(heap, -num)

    answer = 0

    while queue:
        idx, priority = queue.popleft()

        if priority < -heap[0]:
            queue.append((idx, priority))
        else:
            heapq.heappop(heap)
            answer += 1

            if idx == location:
                return answer