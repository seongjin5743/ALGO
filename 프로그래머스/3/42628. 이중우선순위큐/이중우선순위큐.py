import heapq

def solution(operations):
    queue = []

    for op in operations:
        cmd, num = op.split()
        num = int(num)

        if cmd == 'I':
            heapq.heappush(queue, num)

        elif queue:
            if num == -1:
                heapq.heappop(queue)
            else:
                queue.remove(max(queue))
                heapq.heapify(queue)

    if not queue:
        return [0, 0]

    return [max(queue), queue[0]]