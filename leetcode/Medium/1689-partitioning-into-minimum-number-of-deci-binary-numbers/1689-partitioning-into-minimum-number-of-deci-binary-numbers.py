class Solution:
    def minPartitions(self, n: str) -> int:
        return max(map(int, list(n)))