def solution(n, results):
    answer = 0
    
    distance = [[0] * n for _ in range(n)]
    
    for x, y in results:
        distance[x - 1][y - 1] = 1
        distance[y - 1][x - 1] = -1
        
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if distance[i][k] == distance[k][j] == 1:
                    distance[i][j] = 1
                elif distance[i][k] == distance[k][j] == -1:
                    distance[i][j] = -1
    for result in distance:
        if result.count(0) == 1:
            answer += 1

    return answer