def solution(msg):
    answer = []

    alphabet_dict = {chr(i): i - 64 for i in range(65, 91)}
    next_num = 27
    start = 0
    
    while start < len(msg):
        end = start + 1
        
        while end <= len(msg) and msg[start:end] in alphabet_dict:
            end += 1
            
        current_word = msg[start:end-1]
        answer.append(alphabet_dict[current_word])
        
        if end <= len(msg):
            new_word = msg[start:end]
            alphabet_dict[new_word] = next_num
            next_num += 1

        start = end - 1
        
    return answer