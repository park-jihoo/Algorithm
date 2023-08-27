def solution(people, limit):
    people.sort()
    length = len(people)
    light = 0
    heavy = length - 1
    cnt = 0
    while light < heavy:
        if people[light] + people[heavy] <= limit:
            cnt += 1
            light += 1
            heavy -= 1
        else:
            heavy -= 1
    return length - cnt
