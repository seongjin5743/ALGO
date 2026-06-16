def solution(myString):
    answer = list(myString.split('x'))
    result = []
    for i in answer:
        result.append(len(i))
    return result