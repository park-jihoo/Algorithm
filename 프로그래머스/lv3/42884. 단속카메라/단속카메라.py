def solution(routes):
    answer = 1
    routes = sorted(routes)
    cPosition = routes[0][1]
    for i in range(1, len(routes)):
        if routes[i][1] < cPosition:
            cPosition = routes[i][1]
        if routes[i][0] > cPosition:
            answer += 1
            cPosition = routes[i][1]
    return answer
