n, s = map(int, input().split())
nums = list(map(int, input().split()))

count = 0

def recur(idx, total):
    global count
    if idx == n:
        if total == s:
            count += 1
        return
    
    recur(idx + 1, total + nums[idx])
    recur(idx + 1, total)

recur(0, 0)

if s == 0:
    count -= 1

print(count)