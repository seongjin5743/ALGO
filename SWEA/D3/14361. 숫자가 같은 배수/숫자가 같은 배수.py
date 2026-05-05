T = int(input())

for t in range(1, T + 1):
    N = int(input())
    N_lst = list(str(N).strip())
    N_lst.sort()
    flag = False
    k = 2
    while True:
        num = N * k
        num_lst = list(str(num).strip())
        if len(num_lst) > len(N_lst):
            break
        if sorted(num_lst) == N_lst:
            flag = True
            break

        k += 1
    
    answer = 'possible' if flag else 'impossible'
    print(f"#{t} {answer}")