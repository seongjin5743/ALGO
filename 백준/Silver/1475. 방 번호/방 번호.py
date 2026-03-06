n = input()

s = dict()

for num in n:
    num = int(num)

    if num == 6:
        num = 9

    if num not in s:
        s[num] = 1
    else:
        s[num] += 1

if 9 in s:
    s[9] = (s[9] + 1) // 2

print(max(list(s.values())))