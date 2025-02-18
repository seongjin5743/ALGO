def solution(num_list):
    return num_list[::-1]

def solution1(num_list):
    num_list.reverse()
    return num_list

def solution2(num_list):
    result = []
    for num in num_list:
        result.insert(0, num)
    return result