class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        answer = 0
        zerostart = None
        for idx, val in enumerate(nums):
            if val == 0:
                answer += 1
                if zerostart is not None:
                    answer += idx - zerostart
                else:
                    zerostart = idx
            else:
                zerostart = None

        return answer
