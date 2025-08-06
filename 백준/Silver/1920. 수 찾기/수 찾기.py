n = int(input())
nlist = list(map(int, input().split()))
m = int(input())
mlist = list(map(int, input().split()))

def search(array, start, end, target):
    if start > end:
        return 0
    
    mid = (start + end) // 2

    if array[mid] == target:
        return 1
    elif array[mid] > target:
        return search(array, start, mid - 1, target)
    else:
        return search(array, mid + 1, end, target)

nlist.sort()

for i in range(m):
    print(search(nlist, 0, len(nlist) - 1, mlist[i]))