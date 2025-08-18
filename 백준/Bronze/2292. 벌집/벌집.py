n = int(input())

count = 1
room = 1
sixs = 0

while n > room:
    count += 1
    sixs += 6
    room += sixs

print(count)