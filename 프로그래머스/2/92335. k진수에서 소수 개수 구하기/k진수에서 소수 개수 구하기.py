def is_prime(num):
    if num < 2:
        return False

    for j in range(2, int(num ** 0.5) + 1):
        if num % j == 0:
            return False
    return True

def solution(n, k):
    num = ''

    while n > 0:
        num += str(n % k)
        n = n // k
    num = num[::-1]

    lst = [int(i) for i in num.split('0') if i != '']

    cnt = 0
    for x in lst:
        if is_prime(x):
            cnt += 1
            
    return cnt