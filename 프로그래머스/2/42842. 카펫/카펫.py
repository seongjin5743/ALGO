def solution(brown, yellow):
    result = brown + yellow
    
    answer = []
    
    for i in range(3, result + 1):
        if result % i == 0:
            if yellow == (i - 2) * (result // i - 2):
                return sorted([i, result // i], reverse = True)