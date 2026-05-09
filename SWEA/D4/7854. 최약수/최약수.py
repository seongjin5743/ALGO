T = int(input())

nums = []

for i in range(10):
    nums.append(10 ** i)

for i in range(9):
    nums.append(2 * (10 ** i))

for i in range(9):
    nums.append(5 * (10 ** i))

for i in range(8):
    nums.append(25 * (10 ** i))

for i in range(7):
    nums.append(125 * (10 ** i))

nums.sort()

for t in range(1, T + 1):
    x = int(input())

    cnt = 0
    for num in nums:
        if num <= x:
            cnt += 1

    print(f"#{t} {cnt}")