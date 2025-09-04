p, m = map(int, input().split())

charactor = []
for _ in range(p):
    l, n = input().split()
    charactor.append((int(l), n))

start_num = charactor[0][0]

while charactor:
    j = 0
    new_list = []
    removed = []

    for num, name in charactor:
        if start_num - 10 <= num <= start_num + 10 and j < m:
            removed.append((num, name))
            j += 1
        else:
            new_list.append((num, name))

    if len(removed) == m:
        print("Started!")
    else:
        print("Waiting!")

    for num, name in sorted(removed, key=lambda x: x[1]):
        print(num, name)

    charactor = new_list
    if charactor:
        start_num = charactor[0][0]