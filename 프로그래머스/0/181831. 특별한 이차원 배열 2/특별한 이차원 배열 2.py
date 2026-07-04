def solution(arr):
    for j in range(len(arr)):
        for i in range(len(arr[0])):
            if arr[j][i] != arr[i][j]:
                return 0
    return 1