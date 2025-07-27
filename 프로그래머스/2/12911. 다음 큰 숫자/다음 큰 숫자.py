def solution(n):
    nums = list(str(bin(n)))
    x = 1
    while nums.count('1') != list(str(bin(n + x))).count('1'):
        x += 1
    return n + x
