def solution(bridge_length, weight, truck_weights):
    truck_weights[::-1]
    n=len(truck_weights)
    passing_weight=[0]*n
    passed=[]
    passing=[]
    i=0
    j=-1
    while len(passed)<n:
        if(len(truck_weights)>0 and sum(passing)+truck_weights[-1]<=weight):
            passing.append(truck_weights.pop())
            j+=1
        passing_weight[:j+1]=[passing_weight[z]+1 for z in range(j+1)]
        if passing_weight[i]==bridge_length:
            passed.append(passing[0])
            passing=passing[1:]
            i+=1
    return passing_weight[0]+1