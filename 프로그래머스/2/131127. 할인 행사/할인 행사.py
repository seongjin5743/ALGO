def solution(want, number, discount):
    want = [want[i] for i in range(len(want)) for _ in range(number[i])]
    want.sort()
    answer = 0
    for i in range(len(discount) - 9):
        temp = discount[i:i+10]
        temp.sort()
        if temp == want:
            answer += 1
    return answer
