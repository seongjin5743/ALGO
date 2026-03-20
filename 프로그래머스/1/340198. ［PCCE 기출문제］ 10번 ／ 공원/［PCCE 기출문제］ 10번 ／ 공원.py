def solution(mats, park):
    mats.sort(reverse=True)

    dx, dy = len(park[0]), len(park)

    for mat in mats:
        for y in range(dy - mat + 1):
            for x in range(dx - mat + 1):
                if all(park[y + i][x + j] == "-1" for i in range(mat) for j in range(mat)):
                    return mat
    
    return -1