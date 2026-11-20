from collections import deque

def solution(begin, target, words):
    if target not in words:
        return 0

    visited = [False] * len(words)
    queue = deque([(begin, 0)])

    while queue:
        word, count = queue.popleft()
        
        if word == target:
            return count
        
        for i in range(len(words)):
            if not visited[i]:
                
                diff = 0
                for j in range(len(word)):
                    if word[j] != words[i][j]:
                        diff += 1
                if diff == 1:
                    queue.append((words[i], count + 1))
                    visited[i] = True

    return 0