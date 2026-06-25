import heapq

def solution(jobs):
    jobs.sort(key=lambda x: x[0])
    
    answer = 0
    start = 0
    i = 0
    count = 0
    queue = []
    
    while count < len(jobs):

        while i < len(jobs) and jobs[i][0] <= start:
            heapq.heappush(queue, (jobs[i][1], jobs[i][0]))
            i += 1
        
        if queue:
            time, n_start = heapq.heappop(queue)

            answer += (start - n_start) + time

            start += time
            count += 1
        else:
            start = jobs[i][0]
            
    return answer // len(jobs)