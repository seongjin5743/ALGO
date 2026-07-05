def solution(arr, flag):
    answer = []
    for i, j in zip(arr, flag):
        if j == True:
            for k in range(2*i):
                answer.append(i)
        if j == False:
            for k in range(i):
                answer.pop()

    return answer