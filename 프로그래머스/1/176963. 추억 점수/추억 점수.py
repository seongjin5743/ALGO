def solution(name, yearning, photo):
    result = []
    answer = {}
    for i in range(len(name)):
        answer[name[i]] = yearning[i]
    for pho in (photo):
        ans = 0
        for i in range(len(pho)):
            if pho[i] in name:
                ans += answer[pho[i]]
        result.append(ans)
    return result