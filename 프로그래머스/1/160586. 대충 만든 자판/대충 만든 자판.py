def solution(keymap, targets):
    answer = []
    key_dict = {}
    
    for key in keymap:
        for idx, char in enumerate(key):
            if char not in key_dict:
                key_dict[char] = idx + 1
            else:
                key_dict[char] = min(key_dict[char], idx + 1)

    for target in targets:
        total_press = 0
        is_possible = True
        
        for char in target:
            if char in key_dict:
                total_press += key_dict[char]
            else:
                is_possible = False
                break
                
        if is_possible:
            answer.append(total_press)
        else:
            answer.append(-1)
            
    return answer