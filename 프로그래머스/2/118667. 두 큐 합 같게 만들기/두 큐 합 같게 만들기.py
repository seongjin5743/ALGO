from collections import deque

def solution(queue1, queue2):
    q1 = deque(queue1)
    q2 = deque(queue2)
    
    sum1 = sum(q1)
    sum2 = sum(q2)
    
    if (sum1 + sum2) % 2 != 0:
        return -1
        
    answer = 0

    limit = len(queue1) * 4
    
    while sum1 != sum2:
        if answer > limit:
            return -1
            
        if sum1 > sum2:
            temp = q1.popleft()
            sum1 -= temp
            sum2 += temp
            q2.append(temp)
        else:
            temp = q2.popleft()
            sum2 -= temp
            sum1 += temp
            q1.append(temp)
            
        answer += 1
        
    return answer