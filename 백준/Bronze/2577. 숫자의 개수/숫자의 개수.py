A = int(input())
B = int(input())
C = int(input())

answer = str(A * B * C)

result = [0] * 10

for ans in answer:
    result[int(ans)] += 1

for r in result:
    print(r)