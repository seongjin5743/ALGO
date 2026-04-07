import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    oxs = list(input())
    
    again = 0
    answer = 0
    for ox in oxs:
        if ox == 'O':
            again += 1
            answer += again
        if ox == 'X':
            again = 0
    print(answer)