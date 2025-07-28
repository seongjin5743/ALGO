def solution(n,a,b):
    answer = [0] * n
    answer[a - 1] = 1
    answer[b - 1] = 1
    qwer = 0
    while answer.count(2) == 0:
        count = []
        for i in range(0, len(answer) - 1 , 2):
            count.append(answer[i] + answer[i + 1])
        answer = count
        qwer += 1
    return qwer