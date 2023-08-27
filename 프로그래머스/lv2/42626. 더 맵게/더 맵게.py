import heapq
def solution(scoville, K):
    heap=[]
    answer=0
    heapq.heapify(scoville)
    while len(scoville)>1:
        a=heapq.heappop(scoville)
        b=heapq.heappop(scoville)
        if a<K or b<K:
            heapq.heappush(scoville, a+b*2)
            answer=answer+1
        else:
            return answer
    if scoville[0]>K:
        return answer
    else:
        return -1