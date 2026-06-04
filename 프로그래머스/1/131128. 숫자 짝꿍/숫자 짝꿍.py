def solution(X, Y):
    answer = ''
    x_c = {}
    y_c = {}
    
    for x in X:
        if x not in x_c:
            x_c[x] = 1
        else:
            x_c[x] += 1
    for y in Y:
        if y not in y_c:
            y_c[y] = 1
        else:
            y_c[y] += 1
    
    for i in range(9, -1, -1):
        temp = str(i)
        if temp in x_c and temp in y_c:
            answer += temp * min(x_c[temp], y_c[temp])
            
    if not answer:
        answer = '-1'
        
    if all(c == '0' for c in answer):
        answer = '0'

    return answer