def solution(survey, choices):
    answer = ''

    mbti = {'R': 0, 'T': 0, 
            'C': 0, 'F': 0, 
            'J': 0, 'M': 0, 
            'A': 0, 'N': 0}
    for i in range(len(survey)):
        a, b = survey[i]
        if choices[i] - 4 == 0:
            continue
        elif choices[i] - 4 > 0:
            mbti[b] += choices[i] - 4
        else:
            mbti[a] -= choices[i] - 4
    
    if mbti['R'] == mbti['T']:
        answer += 'R'
    elif mbti['R'] > mbti['T']:
        answer += 'R'
    else:
        answer += 'T'

    if mbti['C'] == mbti['F']:
        answer += 'C'
    elif mbti['C'] > mbti['F']:
        answer += 'C'
    else:
        answer += 'F'

    if mbti['J'] == mbti['M']:
        answer += 'J'
    elif mbti['J'] > mbti['M']:
        answer += 'J'
    else:
        answer += 'M'  

    if mbti['A'] == mbti['N']:
        answer += 'A'
    elif mbti['A'] > mbti['N']:
        answer += 'A'
    else:
        answer += 'N'  
        
    return answer