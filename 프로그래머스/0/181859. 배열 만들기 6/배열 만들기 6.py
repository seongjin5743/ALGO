def solution(arr):
    i = 0
    stk = []
    for num in arr:
        if len(stk) == 0:
            stk.append(num)
            i += 1
        elif len(stk) != 0 and stk[-1] == num:
            stk.pop()
            i += 1
        else:
            stk.append(num)
            i += 1
    return stk if stk else [-1]