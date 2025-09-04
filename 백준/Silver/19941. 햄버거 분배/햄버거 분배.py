n, k = map(int, input().split())
table = list(input())

hamburger_index = []
people_index = []

for i in range(n):
    if table[i] == 'H':
        hamburger_index.append(i)
    else:
        people_index.append(i)

count = 0
j = 0
for person in people_index:
    while j < len(hamburger_index) and hamburger_index[j] < person - k:
        j += 1
    if j < len(hamburger_index) and abs(hamburger_index[j] - person) <= k:
        count += 1
        j += 1
print(count)