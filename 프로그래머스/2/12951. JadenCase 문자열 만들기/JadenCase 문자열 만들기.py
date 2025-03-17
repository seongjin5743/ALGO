def solution(s):
    answer = ''
    s = list(s)
    s[0] = s[0].upper()
    answer += s[0]
    for i in range(1, len(s)):
        if s[i - 1] ==' ':
            s[i] = s[i].upper()
        else:
            s[i] = s[i].lower()
        answer += s[i]
    return answer