import heapq

def solution(n, works):
    if sum(works) <= n:
        return 0
    
    heap = []
    for work in works:
        heapq.heappush(heap, -work)
    
    for _ in range(n):
        max_work = -heapq.heappop(heap)
        max_work -= 1
        heapq.heappush(heap, -max_work)
    
    return sum(x*x for x in heap)