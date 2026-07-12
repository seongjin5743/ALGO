def solution(arr):
    num = 1
    while num < len(arr):
        num *= 2
    return arr + [0] * (num - len(arr))