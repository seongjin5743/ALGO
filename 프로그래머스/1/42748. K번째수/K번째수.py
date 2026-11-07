def solution(array, commands):
    answer = []
    for i, j, k in commands:
        n_arr = sorted(array[i-1:j])
        answer.append(n_arr[k-1])
    return answer