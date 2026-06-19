def solution(my_string, is_prefix):
    return 1 if my_string[0:len(is_prefix)] == is_prefix else 0