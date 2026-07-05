def solution(strArr):
    answer = {}
    for s in strArr:
        if len(s) not in answer:
            answer[len(s)] = 1
        else:
            answer[len(s)] += 1
    
    return max(answer.values())