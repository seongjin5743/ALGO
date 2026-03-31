def solution(new_id):
    
    def recommend(x, new_id):
        if x == 1:
            return new_id.lower()
        
        elif x == 2:
            answer = ''
            for c in new_id:
                if c.isalnum() or c in ['-', '_', '.']:
                    answer += c
            return answer
        
        elif x == 3:
            while '..' in new_id:
                new_id = new_id.replace('..', '.')
            return new_id
        
        elif x == 4:
            return new_id.strip('.')
        
        elif x == 5:
            return new_id if new_id else 'a'
        
        elif x == 6:
            new_id = new_id[:15]
            return new_id.rstrip('.')
        
        elif x == 7:
            while len(new_id) < 3:
                new_id += new_id[-1]
            return new_id
    
    for i in range(1, 8):
        new_id = recommend(i, new_id)
        
    return new_id