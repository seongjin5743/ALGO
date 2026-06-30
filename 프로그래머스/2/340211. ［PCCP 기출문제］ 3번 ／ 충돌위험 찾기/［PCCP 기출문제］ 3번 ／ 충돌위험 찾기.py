from collections import deque, defaultdict

def solution(points, routes):
    answer = 0

    def bfs(s_x, s_y, e_x, e_y):
        queue = deque()
        queue.append((s_x, s_y, [(s_y, s_x)]))
        
        while queue:
            x, y, lst = queue.popleft()
            
            if x == e_x and y == e_y:
                return lst

            if y != e_y:
                nx, ny = x, y + (1 if e_y > y else -1)
            else:
                nx, ny = x + (1 if e_x > x else -1), y

            queue.append((nx, ny, lst + [(ny, nx)]))

    all_robot_paths = []

    for route in routes:
        robot_path = []
        for i in range(len(route) - 1):
            a = route[i]
            b = route[i + 1]
            
            s_y, s_x = points[a - 1]
            e_y, e_x = points[b - 1]
            
            path = bfs(s_x, s_y, e_x, e_y)

            if i == 0:
                robot_path.extend(path)
            else:
                robot_path.extend(path[1:])
                
        all_robot_paths.append(robot_path)
            
    max_time = max(len(p) for p in all_robot_paths)
    
    for t in range(max_time):
        time_map = defaultdict(int)
        
        for path in all_robot_paths:
            if t < len(path):
                time_map[path[t]] += 1
                
        for count in time_map.values():
            if count >= 2:
                answer += 1
                
    return answer