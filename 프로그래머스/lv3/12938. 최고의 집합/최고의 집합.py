def solution(n, s):
    if n > s:
        return [-1]
    [portion, remain] = divmod(s, n)
    answer = [portion] * n
    for i in range(remain):
        answer[i] += 1
    return sorted(answer)
