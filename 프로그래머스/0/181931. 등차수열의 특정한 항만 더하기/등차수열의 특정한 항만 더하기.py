def solution(a, d, included):
    answer = [a] + [a + i for i in range(d, (len(included) - 1) * d + 1, d)]
    result = 0
    for i in range(len(included)):
        if included[i]:
            result += answer[i]
    return result