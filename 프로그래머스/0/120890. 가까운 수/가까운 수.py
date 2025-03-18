def solution(array, n):
    array.append(n)
    array.sort()
    
    idx = array.index(n)
    
    if idx == 0:
        return array[1]
    elif idx == len(array) - 1:
        return array[-2]
    else:
        
        left = array[idx - 1]
        right = array[idx + 1]
       
        return left if abs(left - n) <= abs(right - n) else right
