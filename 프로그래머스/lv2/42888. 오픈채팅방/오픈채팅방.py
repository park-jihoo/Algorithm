def solution(record):
    answer = []
    idname = {}
    loglist = []
    for i in record:
        log = i.split()
        if log[0] == 'Enter':
            idname[log[1]] = log[2]
            loglist.append([log[1], '님이 들어왔습니다.'])
        if log[0] == 'Change':
            idname[log[1]] = log[2]
        if log[0] == 'Leave':
            loglist.append([log[1], '님이 나갔습니다.'])

    return [idname[x[0]]+x[1] for x in loglist]