def solution(s):
    answer = []
    check = set()

    arr = s.replace('{{','').replace('}}','').split('},{')
    arr.sort(key=lambda x: len(x))

    for x in arr:
        temp = x.split(',')

        for num in temp:
            num = int(num)

            if num not in check:
                check.add(num)
                answer.append(num)

    return answer