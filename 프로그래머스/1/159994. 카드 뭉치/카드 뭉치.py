def solution(cards1, cards2, goal):
    answer = ''
    
    for i in range(len(goal)):
        if goal[i] in cards1 :
            if cards1.index(goal[i]) == 0:
                cards1.pop(0)
            else: 
                return 'No'
                
        elif goal[i] in cards2:
            if cards2.index(goal[i]) == 0:
                cards2.pop(0)
            else: 
                return 'No'
        else:
            return 'No'
    return 'Yes'