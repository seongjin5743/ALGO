def solution(n):
    answer = 0
    n = str(n)
    for i in n:
        answer += int(i)
    return answer

def solution1(n):
    answer = 0
    while n > 0:
        a, b = divmod(n, 10)
        answer += b
        n = a
    return answer