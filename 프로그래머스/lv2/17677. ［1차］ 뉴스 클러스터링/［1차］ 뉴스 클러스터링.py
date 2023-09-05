def intersect(a, b):
    result = []
    a_temp = a.copy()
    for i in b:
        if i in a_temp:
            a_temp.remove(i)
            result.append(i)
    return len(result)


def plus(a, b):
    a_temp = a.copy()
    a_result = a.copy()
    for i in b:
        if i not in a_temp:
            a_result.append(i)
        else:
            a_temp.remove(i)
    return len(a_result)


def solution(str1, str2):
    str1, str2 = str1.lower(), str2.lower()
    list1 = [
        str1[x] + str1[x + 1]
        for x in range(len(str1) - 1)
        if "a" <= str1[x] <= "z" and "a" <= str1[x + 1] <= "z"
    ]
    list2 = [
        str2[x] + str2[x + 1]
        for x in range(len(str2) - 1)
        if "a" <= str2[x] <= "z" and "a" <= str2[x + 1] <= "z"
    ]
    a, b = intersect(list1, list2), plus(list1, list2)
    if a == b:
        return 65536
    return int(65536 * a / b)
