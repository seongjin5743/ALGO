t = int(input())

for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))

    max_num = 0

    answer = 0
    for i in range(len(nums) - 1, -1, -1):
        if max_num < nums[i]:
            max_num = nums[i]
        else:
            answer += (max_num - nums[i])
    print(answer)