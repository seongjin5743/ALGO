import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))

prefixSum = [0] * (n + 1)
prefixSum[1] = nums[0]
for k in range(2, n + 1):
    prefixSum[k] = prefixSum[k - 1] + nums[k - 1]

for _ in range(m):
    i, j = map(int, input().split())
    print(prefixSum[j] - prefixSum[i - 1])