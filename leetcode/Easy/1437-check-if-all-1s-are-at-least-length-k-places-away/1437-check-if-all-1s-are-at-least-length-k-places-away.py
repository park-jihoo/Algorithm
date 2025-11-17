class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        ones = [idx for idx, val in enumerate(nums) if val == 1]
        for i in range(len(ones) - 1):
            if ones[i+1] - ones[i] - 1 < k:
                return False
        return True