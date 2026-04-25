t = int(input())

color = [input().split() for _ in range(t)]

lst = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']

for c1, c2 in color:
    if c1 == c2:
        print('E')
    else:
        num1, num2 = 0, 0
        for i in range(6):
            if lst[i] == c1:
                num1 = i
            if lst[i] == c2:
                num2 = i
        num = abs(num1 - num2)

        if num == 1 or num == 5:
            print('A')
        elif num == 3:
            print('C')
        else:
            print('X')
