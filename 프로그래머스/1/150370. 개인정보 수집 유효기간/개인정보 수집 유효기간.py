def solution(today, terms, privacies):
    answer = []
    
    term = dict()
    
    for t in terms:
        x, y = t.split(' ')
        term[x] = int(y) * 28
        
        
    y, m, d = map(int, today.split('.'))
    t = y * 28 * 12 + m * 28 + d
    
    for i in range(len(privacies)):
        day, te = privacies[i].split(' ')
        y, m, d = map(int, day.split('.'))
        n_t = y * 28 * 12 + m * 28 + d
        
        if n_t + term[te] <= t:
            answer.append(i + 1)
    return answer