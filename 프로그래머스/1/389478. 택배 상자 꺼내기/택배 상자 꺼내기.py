def solution(n, w, num):
    answer = 0
    
    box = []
    for i in range(1, n + 1, w):
        row = list(range(i, min(i + w, n + 1)))
        
        if len(box) % 2 == 1:
            row.reverse()
            if len(row) < w:
                row = [0] * (w - len(row)) + row
        else:
            if len(row) < w:
                row = row + [0] * (w - len(row))
            
        box.append(row)
        
    for r in range(len(box)):
        if num in box[r]:
            c = box[r].index(num)
            break
            
    for i in range(r, len(box)):
        if box[i][c] != 0:
            answer += 1
            
    return answer