import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    y = input().strip()
    
    last_two = int(y[-2:])
    y_int = int(y)

    if (y_int + 1) % last_two == 0:
        print('Good')
    else:
        print('Bye')