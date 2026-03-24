def solution(friends, gifts):
    answer = 0
    
    give = dict()
    receive = dict()
    
    for friend in friends:
        give[friend] = []
        receive[friend] = []
    
    for gift in gifts:
        g, r = gift.split(' ')
        
        give[g].append(r)
        receive[r].append(g)
    
    score = dict()
    present = dict()
    
    for friend in friends:
        score[friend] = len(give[friend]) - len(receive[friend])
        present[friend] = 0
    
    for g_friend in friends:
        for r_friend in friends:
            if g_friend == r_friend:
                continue
            
            g_cnt = give[g_friend].count(r_friend)
            r_cnt = give[r_friend].count(g_friend)
            
            if g_cnt > r_cnt:
                present[g_friend] += 1
            elif g_cnt == r_cnt:
                if score[g_friend] > score[r_friend]:
                    present[g_friend] += 1
                    
    return max(present.values())