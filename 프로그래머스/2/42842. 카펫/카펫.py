def solution(brown, yellow):
    space = brown + yellow
    
    for i in range(3, space + 1):
        if space % i == 0:
            if yellow == (i - 2) * (space // i - 2):
                return sorted([i, space // i], reverse = True)