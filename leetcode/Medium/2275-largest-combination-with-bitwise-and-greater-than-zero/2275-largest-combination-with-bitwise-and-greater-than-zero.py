class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        bit = [0]*24
        for i in range(24):
            for num in candidates:
                if (num & (1<<i)) != 0:
                    bit[i] += 1
        return max(bit)