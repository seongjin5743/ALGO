def solution(s):
    qwer=list(map(int,s.split()))
    
    return str(min(qwer)) + " " + str(max(qwer))