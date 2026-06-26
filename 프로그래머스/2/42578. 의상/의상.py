def solution(clothes):
    cloth = {}
    
    for name, category in clothes:
        if category not in cloth:
            cloth[category] = 1
        else:
            cloth[category] += 1
    
    answer = 1
    
    for category in cloth:
        answer *= (cloth[category] + 1)
        
    return answer - 1