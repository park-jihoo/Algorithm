def solution(number, k):
    number=list(number)
    answer=[number[0]]
    Tos=0
    for i in range(1, len(number)):
        answer.append(number[i])
        Tos+=1
        correct=1
        while(correct and k!=0):
            correct-=1
            for j in range(Tos, len(answer)):
                if answer[j-1]>=answer[j]:
                    pass
                else:
                    answer[j-1],answer[j]=answer[j],answer[j-1]
                    answer.pop()
                    correct+=1
                    Tos-=1
                    k-=1
                    break
    answer="".join(answer)
    return answer[:len(answer)-k]