def solution(k, tangerine):
    answer = 1
    size_count = {}
    for size in tangerine:
        if size in size_count:
            size_count[size] += 1
        else:
            size_count[size] = 1
    sorted_sizes = sorted(size_count.values(), reverse=True)
    for i in range(len(sorted_sizes)):
        if k > sorted_sizes[i]:
            k -= sorted_sizes[i]
            answer += 1
        else:
            break
    return answer