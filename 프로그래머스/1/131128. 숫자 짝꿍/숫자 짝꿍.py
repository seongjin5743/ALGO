from collections import Counter

def solution(X, Y):
    answer = ''
    x_c = Counter(X)
    y_c = Counter(Y)
    
    for i in range(9, -1, -1):
        temp = str(i)
        if temp in x_c and temp in y_c:
            answer += temp * min(x_c[temp], y_c[temp])
            
    if not answer:
        answer = '-1'
        
    if all(c == '0' for c in answer):
        answer = '0'

    return answer