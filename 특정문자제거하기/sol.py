def solution(my_string, letter):
    answer = ''
    for s in my_string:
        if s != letter:
            answer += s
    return answer

def solution1(my_string, letter):
    answer = my_string.replace(letter,'')
    return answer