kdy = [2,2,1,1,-1,-1,-2,-2]
kdx = [1,-1,2,-2,2,-2,1,-1]

knight = [input().strip() for _ in range(36)]

col = {'A':0,'B':1,'C':2,'D':3,'E':4,'F':5}
row = {'1':0,'2':1,'3':2,'4':3,'5':4,'6':5}

visited = set()

sx = col[knight[0][0]]
sy = row[knight[0][1]]

px, py = sx, sy
visited.add((px, py))

valid = True

for i in range(1, 36):
    nx = col[knight[i][0]]
    ny = row[knight[i][1]]

    if (nx, ny) in visited:
        valid = False
        break

    move = False
    for d in range(8):
        if px + kdx[d] == nx and py + kdy[d] == ny:
            move = True
            break

    if not move:
        valid = False
        break

    visited.add((nx, ny))
    px, py = nx, ny

if valid:
    move = False
    for d in range(8):
        if px + kdx[d] == sx and py + kdy[d] == sy:
            move = True
            break
    if not move:
        valid = False

print("Valid" if valid else "Invalid")