def solution(lottos, win_nums):
    answer = [0,0]
    notzero = set([x for x in lottos if x != 0])
    minnum = len(set(win_nums) & notzero)
    maxnum = minnum + 6 - len(notzero)
    print(minnum, maxnum)
    if minnum == 0:
        answer[1] = 6
    else:
        answer[1] = 7 - minnum
    if maxnum == 0:
        answer[0] = 6
    else:
        answer[0] = 7 - maxnum
    return answer