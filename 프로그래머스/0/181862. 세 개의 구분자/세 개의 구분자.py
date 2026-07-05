import re

def solution(myStr):
    tokens = re.split('[abc]', myStr)
    
    answer = [x for x in tokens if x]
    
    return answer if answer else ["EMPTY"]