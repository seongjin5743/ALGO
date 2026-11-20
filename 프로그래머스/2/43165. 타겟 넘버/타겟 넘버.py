def solution(numbers, target):
    def dfs(x, current):
        if x == len(numbers):
            if current == target:
                return 1
            else:
                return 0
        
        return dfs(x + 1, current + numbers[x]) + dfs(x + 1, current - numbers[x])
    return dfs(0,0)