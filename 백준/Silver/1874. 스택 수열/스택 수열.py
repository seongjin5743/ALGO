import sys

input = sys.stdin.readline

n = int(input())

stack = []
answer = []
temp = True
count = 1
for _ in range(n):
    num = int(input())

    while count <= num:
        stack.append(count)
        answer.append('+')
        count += 1

    if stack[-1] == num:
        stack.pop()
        answer.append('-')
    else:
        temp = False
        break

if not temp:
    print('NO')
else:
    for a in answer:
        print(a)