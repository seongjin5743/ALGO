def solution(spell, dic):
    target = sorted(spell)
    for d in dic:
        if sorted(d) == target:
            return 1
    return 2