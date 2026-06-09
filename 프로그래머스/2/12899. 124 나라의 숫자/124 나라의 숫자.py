def solution(n):
    result = []
    
    while n > 0:
        n -= 1
        result.append('124'[n % 3])
        n //= 3
    
    return ''.join(result[::-1])