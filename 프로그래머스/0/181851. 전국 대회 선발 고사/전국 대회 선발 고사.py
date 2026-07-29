def solution(rank, attendance):
    answer = []
    for i in range(1, len(rank) + 1):
        num = rank.index(i)
        if attendance[num]:
            answer.append(num)
        if len(answer) == 3:
            break
    
    return 10000 * answer[0] + 100 * answer[1] + answer[2]