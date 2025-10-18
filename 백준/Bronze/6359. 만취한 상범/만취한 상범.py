n = int(input())

for _ in range(n):
    num = int(input())
    rooms = [1] * num
    for i in range(1, num + 1):
        for j in range(i, num + 1, i):
            rooms[j - 1] *= -1
    
    print(rooms.count(-1))