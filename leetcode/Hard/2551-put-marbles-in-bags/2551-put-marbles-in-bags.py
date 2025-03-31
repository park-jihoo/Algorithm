class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        marble_pair = [a+b for a, b in pairwise(weights)]
        return sum(heapq.nlargest(k-1, marble_pair)) - sum(heapq.nsmallest(k-1, marble_pair))