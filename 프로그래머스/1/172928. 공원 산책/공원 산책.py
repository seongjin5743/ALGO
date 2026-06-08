def solution(park, routes):
    n, m = len(park), len(park[0])
    x, y = 0, 0
    for ny in range(n):
        for nx in range(m):
            if park[ny][nx] == 'S':
                x, y = nx, ny
                break
    
    dir = {'N': (0,-1), 'S': (0,1), 'W': (-1,0), 'E': (1,0)}
    
    def rou(op, count, x, y):
        dx, dy = dir[op]
        nx, ny = x, y

        for _ in range(count):
            nx += dx
            ny += dy

            if not (0 <= nx < m and 0 <= ny < n) or park[ny][nx] == 'X':
                return x, y

        return nx, ny
    
    for route in routes:
        op, count = route.split()
        x, y = rou(op, int(count), x, y)
        
    return y, x