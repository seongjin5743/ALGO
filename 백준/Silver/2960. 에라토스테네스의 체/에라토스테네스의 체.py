n, k = map(int, input().split())

nums = [i for i in range(2, n + 1)]

sosu = []
count = 0
while nums:
    p = nums[0]

    multiples = [x for x in nums if x % p == 0]
    for m in multiples:
        nums.remove(m)
        sosu.append(m)
        count += 1
        if count == k:
            print(m)
            exit()