t = int(input())

for i in range(1, t + 1):
    n = int(input())
    printer = list(map(int, input().split()))
    
    count = {}
    for p in printer:
        if p in count:
            count[p] += 1
        else:
            count[p] = 1

    answer = []
    
    for p in printer:
        if count[p] == 0:
            continue
        
        if (p * 4) % 3 == 0:
            target = (p * 4) // 3
            
            if target in count and count[target] > 0:
                answer.append(p)
                count[p] -= 1
                count[target] -= 1
    print(f'#{i} ', end='')   
    print(*answer)