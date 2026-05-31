def solution(n):
    answer = ''
    while n > 0:
        n, r = divmod(n, 3)
        answer = str(r) + answer
    return int(answer[::-1], 3)