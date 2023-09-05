def solution(N, stages):
    answer = []
    temp = {}
    gamer = len(stages)
    count = 0
    for i in range(1, N + 1):
        if gamer != 0:
            count = stages.count(i)
            fail = count / gamer
            temp[i] = fail
            gamer -= count

        else:
            temp[i] = 0
    answer = sorted(temp, key=lambda x: temp[x], reverse=True)
    return answer
