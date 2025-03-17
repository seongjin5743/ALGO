def solution(l, r):
    answer = []
    ls1 = {0}
    ls2 = {5}
    ls3 = {0, 5}
    for i in range(l, r + 1):
        num = list(map(int, list(str(i))))
        num = set(num)
        if num == ls1 or num == ls2 or num == ls3:
            answer.append(i)
    if len(answer) == 0:
        return [-1]
    return answer