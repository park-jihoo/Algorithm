def solution(operations):
    answer = []
    for operation in operations:
        if operation[0]=='I':
            answer.append(int(operation[2:]))
        elif operation=="D 1" and len(answer)>0:
            answer.remove(max(answer))
        elif operation=="D -1" and len(answer)>0:
            answer.remove(min(answer))
    if len(answer)==0:
        return [0, 0]
    return [max(answer), min(answer)]