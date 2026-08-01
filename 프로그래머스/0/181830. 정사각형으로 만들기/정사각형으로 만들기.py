def solution(arr):
    a, b = len(arr), len(arr[0])
    if a == b:
        return arr
    elif a > b:
        for i in range(a):
            arr[i] += [0] * (a - b)
    else:
        for _ in range(b - a):
            arr.append([0 for _ in range(b)])
    return arr