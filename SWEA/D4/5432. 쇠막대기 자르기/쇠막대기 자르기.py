T = int(input())

for t in range(1, T + 1):
    tc = input()

    stack = []
    answer = 0

    for i in range(len(tc)):

        if tc[i] == '(':
            stack.append('(')

        else:
            stack.pop()

            if tc[i - 1] == '(':
                answer += len(stack)
            else:
                answer += 1

    print(f'#{t} {answer}')