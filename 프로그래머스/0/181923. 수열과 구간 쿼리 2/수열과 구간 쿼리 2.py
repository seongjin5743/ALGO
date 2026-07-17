def solution(arr, queries):
    answer = []
    for x, y, n in queries:
        a = 1e6
        for i in range(x, y + 1):
            if arr[i] > n:
                a = min(a, arr[i])
        if a == 1e6:
            answer.append(-1)
        else:
            answer.append(a)
    return answer