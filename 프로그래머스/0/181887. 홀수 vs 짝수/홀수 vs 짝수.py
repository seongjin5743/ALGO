def solution(num_list):
    answer = 0
    answer1 = 0
    for i in range(len(num_list)):
        if (i + 1) % 2 == 0:
            answer += num_list[i]
        else:
            answer1 += num_list[i]
    return answer if answer > answer1 else answer1