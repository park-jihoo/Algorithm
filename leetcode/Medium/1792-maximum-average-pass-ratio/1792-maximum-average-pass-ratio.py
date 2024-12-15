class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        pq = []
        n = len(classes)
        for pc, ac in classes:
            heapq.heappush(pq, [(pc/ac)-(pc+1)/(ac+1), (pc, ac)])
        
        for i in range(extraStudents):
            val, (pc, ac) = heapq.heappop(pq)
            pc += 1
            ac += 1
            heapq.heappush(pq, [(pc/ac)-(pc+1)/(ac+1), (pc, ac)])

        return sum(x/y for val, (x, y) in pq) / n