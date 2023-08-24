def solution(numbers, target):
    answer=1
    if len(numbers)==1:
        if numbers[0]==target or numbers[0] == -1*target:
            return 1
        else:
            return 0
    else:
        temp=numbers[:]
        a=temp.pop()
        return solution(temp, target+a)+solution(temp, target-a)
    return answer