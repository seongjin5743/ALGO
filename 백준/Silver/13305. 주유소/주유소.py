n = int(input())

distance = list(map(int, input().split()))

city = list(map(int, input().split()))

answer = 0

for i in range(n - 1):
    if i == 0 and city[i] != min(city[i:n - 1]):
        answer += distance[i] * city[i]
        continue

    if city[i] == min(city[i:n - 1]):
        answer += city[i] * sum(distance[i:n - 1])
        break
    else:
        answer += city[i] * distance[i]
print(answer)