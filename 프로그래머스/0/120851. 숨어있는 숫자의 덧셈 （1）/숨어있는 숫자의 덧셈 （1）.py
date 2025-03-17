def solution(my_string):
    answer = 0
    numbers = '1234567890'
    for m in my_string:
        if m in numbers:
            answer += int(m)
    return answer