import sys
input = sys.stdin.readline
 
N, K = map(int, input().split())
 
ability = [list(map(int, input().split())) for _ in range(N)]
 
first = sorted(ability, key=lambda x: -(x[0] + x[1]))
second = sorted(ability, key=lambda x: -(x[0] + x[2]))
third = sorted(ability, key=lambda x: -(x[1] + x[2]))
 
first_val = 0
second_val = 0
third_val = 0
for i in range(K):
    first_val += first[i][0] + first[i][1]
    second_val += second[i][0] + second[i][2]
    third_val += third[i][1] + third[i][2]
 
result = max(first_val, second_val, third_val)
print(result)