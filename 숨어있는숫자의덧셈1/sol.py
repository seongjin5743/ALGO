def solution(my_string):
    answer = 0
    for m in my_string:
        if m.isdigit():
            answer += int(m)
    return answer

def solution1(my_string):
    answer = 0
    for m in my_string:
        if ord('A') <= ord(m) <= ord('z'):
            continue
        else:
            answer += int(m)
    return answer

def solution2(my_string):
    answer = 0
    numbers = '1234567890'
    for m in my_string:
        if m in numbers:
            answer += int(m)
    return answer

def solution3(my_string):
    answer = 0
    for m in my_string:
        try:
            answer += int(m)
        except:
            continue
    return answer