x,y,z = 1,1,1

tri = []

while x != 0 and y != 0 and z != 0:
    x,y,z = map(int, input().split())
    tri.append((x,y,z))
tri.pop()

for x,y,z in tri:
    if x + y + z - max(x,y,z) <= max(x,y,z):
        print('Invalid')
        continue

    if x == y == z:
        print('Equilateral')
    elif x == y or y == z or z == x:
        print('Isosceles')
    elif x != y != z:
        print('Scalene')