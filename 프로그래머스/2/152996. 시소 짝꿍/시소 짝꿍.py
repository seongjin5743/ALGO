from collections import Counter

def solution(weights):
    answer = 0
    count = Counter(weights)
    
    for w in count:
        answer += count[w] * (count[w] - 1) // 2
        
        for ratio in [(2,1), (3,2), (4,3)]:
            target = w * ratio[0] / ratio[1]
            if target in count:
                answer += count[w] * count[target]
    
    return answer