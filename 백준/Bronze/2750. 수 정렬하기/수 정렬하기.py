n = int(input())

answer = []

for _ in range(n):
    answer.append(int(input()))

answer.sort()

for a in answer:
    print(a)