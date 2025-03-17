def solution(s):
    stack=[]
    for str in s:
        if str=="(":
            stack.append(str)
        elif str==")":
            if not stack:
                return False
            stack.pop()
    return len(stack)==0