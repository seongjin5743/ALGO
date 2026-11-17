T = 10
for test_case in range(1, T + 1):
    answer = 0
    num = int(input())
    buildings = list(map(int, input().split()))
    
    for i in range(2, num - 2):
        if buildings[i] == max(buildings[i-2:i+3]):
            answer += buildings[i] - max(buildings[i-2:i] + buildings[i+1:i+3])
    print(f'#{test_case} {answer}')