import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, k, id, m = map(int, input().split())

    team_list = [[0] * (k + 2) for _ in range(n)]
    latest_list = []
    for _ in range(m):
        i, j, s = map(int, input().split())
        if team_list[i - 1][j - 1] < s:
            team_list[i - 1][j - 1] = s
        
        team_list[i - 1][-2] += 1
        
        if i in latest_list:
            latest_list.remove(i)
        latest_list.append(i)
    
    for i in range(len(latest_list)):
        team_list[latest_list[i] - 1][-1] = i
    
    answer = sorted(team_list, key= lambda x: (-sum(x[:k]), x[-2], x[-1]))

    print(answer.index(team_list[id - 1]) + 1)