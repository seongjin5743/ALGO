import heapq
def solution(scoville, K):
    heapq.heapify(scoville)
    answer = 0
    
    while True:
        if scoville[0] >= K:
            return answer
        
        if len(scoville) == 1:
            return -1
        
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)

        result = first + (second * 2)

        heapq.heappush(scoville, result)
        answer += 1
        
    return answer