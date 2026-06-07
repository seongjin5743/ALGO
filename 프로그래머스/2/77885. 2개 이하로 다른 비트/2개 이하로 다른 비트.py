def solution(numbers):
    answer = []
    for number in numbers:
        if number % 2 == 0:
            answer.append(number + 1)
        else:
            binary = '0' + bin(number)[2:]
            binary = binary[::-1].replace('10', '01', 1)[::-1]
            answer.append(int(binary, 2))
            
    return answer