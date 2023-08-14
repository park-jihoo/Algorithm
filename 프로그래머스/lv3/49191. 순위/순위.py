def solution(n, results):
    answer = 0
    graph1 = {}
    graph2 = {}
    for i in range(n):
        graph1[i + 1] = set()
        graph2[i + 1] = set()
    for i in range(1, n + 1):
        for result in results:
            if result[0] == i:
                graph1[i].add(result[1])
            if result[1] == i:
                graph2[i].add(result[0])
        for winner in graph2[i]:
            graph1[winner].update(graph1[i])
        for loser in graph1[i]:
            graph2[loser].update(graph2[i])
    for i in range(1, n + 1):
        if len(graph1[i]) + len(graph2[i]) == n - 1:
            answer += 1
    return answer
