def solution(arr, k):
    answer = []
    num = 0
    for i in range(len(arr)):
        if arr[i] not in answer:
            answer.append(arr[i])
            num += 1
        
        if num == k:
            return answer
    if len(answer) < k:
        return answer + [-1] * (k - len(answer))