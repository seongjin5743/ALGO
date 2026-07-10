def solution(my_string):
    alphabet_dict = {chr(i): 0 for i in (list(range(65, 91)) + list(range(97, 123)))}
    for s in my_string:
        alphabet_dict[s] += 1
    return list(alphabet_dict.values())