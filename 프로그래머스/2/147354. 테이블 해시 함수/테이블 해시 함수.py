def solution(data, col, row_begin, row_end):
    result = []
    
    data.sort(key=lambda x:(x[col - 1], -x[0]))
    
    for i in range(row_begin - 1, row_end):
        temp = data[i]
        answer = 0
        for t in temp:
            answer += t % (i + 1)
        result.append(answer)
    final_xor = 0
    for num in result:
        final_xor ^= num
    return final_xor