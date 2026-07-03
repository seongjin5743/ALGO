def solution(n):
    i = 1
    fac = 1
    
    while fac * (i + 1) <= n:
        i += 1
        fac *= i
        
    return i