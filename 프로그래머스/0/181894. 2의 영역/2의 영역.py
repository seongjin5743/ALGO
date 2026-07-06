def solution(arr):
    if 2 not in arr:
        return [-1]
    else:
        start_two = arr.index(2)
        for i in range(len(arr)):
            if arr[i] == 2:
                end_two = i
        return arr[start_two:end_two + 1]