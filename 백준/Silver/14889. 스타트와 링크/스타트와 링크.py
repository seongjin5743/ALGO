from itertools import combinations

# 입력
N = int(input())
num = [list(map(int, input().split())) for _ in range(N)]

# 최소 차이를 저장할 변수
min_diff = float('inf')

# 사람들을 두 팀으로 나누는 조합을 구함 (스타트 팀을 선택하는 경우)
for team in combinations(range(N), N // 2):
    start_team = list(team)
    link_team = [i for i in range(N) if i not in start_team]
    
    # 스타트 팀 능력치 계산
    start_score = 0
    for i in start_team:
        for j in start_team:
            if i != j:
                start_score += num[i][j]
    
    # 링크 팀 능력치 계산
    link_score = 0
    for i in link_team:
        for j in link_team:
            if i != j:
                link_score += num[i][j]
    
    # 두 팀의 능력치 차이
    diff = abs(start_score - link_score)
    
    # 최소 차이 갱신
    min_diff = min(min_diff, diff)

# 출력
print(min_diff)