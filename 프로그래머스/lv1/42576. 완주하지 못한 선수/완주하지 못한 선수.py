def solution(participant, completion):
    participant.sort()
    completion.sort()
    for part, comp in zip(participant, completion):
        if part != comp:
            return part

    return participant[-1]
