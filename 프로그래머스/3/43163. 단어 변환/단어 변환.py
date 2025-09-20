from collections import deque

def different(word1, word2):
    if len(word1) != len(word2):
        return False

    diff_count = 0

    for i in range(len(word1)):
        if word1[i] != word2[i]:
            diff_count += 1
            
    return diff_count == 1

def solution(begin, target, words):
    visited = [False] * len(words)
    
    def bfs(word):
        queue = deque()
        queue.append((word, 0))

        while queue:
            nword, cnt = queue.popleft()
            if nword == target:
                return cnt
            for i in range(len(words)):
                if not visited[i] and different(nword, words[i]):
                    visited[i] = True
                    queue.append((words[i], cnt + 1))
        return 0
    return bfs(begin)