def get_divisors(n):
    num = 0
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            num += 1
            if i != n // i:
                num += 1
    return True if num >= 3 else False

def solution(n):
    answer = 0
    for i in range(1, n + 1):
        if get_divisors(i):
            answer += 1
    return answer