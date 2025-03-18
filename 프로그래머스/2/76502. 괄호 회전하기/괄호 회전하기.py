def solution(s):
    answer = 0
    s = list(s)
    
    def is_valid(temp):
        stack = []
        pair = {')': '(', ']': '[', '}': '{'}
        
        for char in temp:
            if char in pair.values():
                stack.append(char)
            elif char in pair.keys():
                if not stack or stack[-1] != pair[char]:
                    return False
                stack.pop()
        
        return len(stack) == 0
    
    for _ in range(len(s)):
        if is_valid(s):
            answer += 1
        s.append(s.pop(0))
    
    return answer
