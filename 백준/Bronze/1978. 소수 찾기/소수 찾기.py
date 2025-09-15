n = int(input())

nums = map(int, input().split())

def sosu(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True

answer = 0
for num in nums:
    if sosu(num):
        answer += 1
print(answer)