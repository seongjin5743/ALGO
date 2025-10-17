import math
import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    nums = list(map(int, input().split()))
    n = nums[0]
    arr = nums[1:]
    answer = 0
    
    for i in range(n):
        for j in range(i + 1, n):
            answer += math.gcd(arr[i], arr[j])
    
    print(answer)