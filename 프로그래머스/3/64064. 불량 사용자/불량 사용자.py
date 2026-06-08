def is_match_manual(user_id, banned_id):
    if len(user_id) != len(banned_id):
        return False
    for i in range(len(user_id)):
        if banned_id[i] == '*':
            continue
        if banned_id[i] != user_id[i]:
            return False
    return True

def solution(user_id, banned_id):
    result = set()
    
    visited = [False] * len(user_id)

    def dfs(banned_index, current_list):

        if banned_index == len(banned_id):
            result.add(tuple(sorted(current_list)))
            return

        current_banned = banned_id[banned_index]
        
        for i in range(len(user_id)):
            if visited[i]:
                continue
                
            if is_match_manual(user_id[i], current_banned):
                visited[i] = True
                current_list.append(user_id[i])
                dfs(banned_index + 1, current_list)
                current_list.pop()
                visited[i] = False

    dfs(0, [])
    
    return len(result)