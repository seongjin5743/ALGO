n, m = map(int, input().split())

a = list(map(int, input().split()))
b = set(map(int, input().split()))

new = [x for x in a if x not in b]

new.sort()
print(len(new))
print(*new)