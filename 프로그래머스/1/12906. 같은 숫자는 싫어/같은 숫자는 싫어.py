def solution(arr):
    answer = [arr[0]]
    for i in range(1, len(arr)):
        num = arr[i]
        if num != answer[-1]:
            answer.append(num)
    return answer
