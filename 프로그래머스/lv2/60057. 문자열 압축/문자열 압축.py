def solution(s):
    length = []
    result = ""
    if len(s) == 1:
        return 1
    for i in range(1, len(s) // 2 + 1):
        count = 1
        tempstr = s[:i]
        for j in range(i, len(s), i):
            if s[j : j + i] == tempstr:
                count += 1
            else:
                if count == 1:
                    count = ""
                result += str(count) + tempstr
                tempstr = s[j : i + j]
                count = 1
        if count == 1:
            count = ""
        result += str(count) + tempstr
        length.append(len(result))
        result = ""
    return min(length)
