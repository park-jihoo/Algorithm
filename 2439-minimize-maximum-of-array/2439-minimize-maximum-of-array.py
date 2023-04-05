import math

class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        curr = 0
        answer = 0
        for idx, val in enumerate(nums):
            curr += val
            avg = math.ceil(curr / (idx + 1))
            answer = max(answer, avg)
                
        return answer