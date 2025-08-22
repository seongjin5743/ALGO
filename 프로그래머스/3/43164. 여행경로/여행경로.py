def solution(tickets):
    answer = []
    graph = {}

    for a, b in tickets:
        if a not in graph:
            graph[a] = []
        graph[a].append(b)
    for k in graph:
        graph[k].sort()

    def dfs(city):
        while graph.get(city):
            next_city = graph[city].pop(0)
            dfs(next_city)
        answer.append(city)

    dfs('ICN')
    return answer[::-1]