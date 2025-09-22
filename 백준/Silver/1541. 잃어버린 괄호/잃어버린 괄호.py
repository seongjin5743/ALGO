sik = input()

answer = sik.split('-')

result = sum(map(int, answer[0].split('+')))

for i in answer[1:]:
    result -= sum(map(int, i.split('+')))

print(result)