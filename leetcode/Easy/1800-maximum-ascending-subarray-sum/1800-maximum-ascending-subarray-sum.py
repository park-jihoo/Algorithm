class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        answer = 0
        temp = 0
        for i in range(len(nums)):
            temp += nums[i]
            if i == len(nums) - 1:
                if temp > answer:
                    return temp
                else:
                    return answer
            if nums[i + 1] <= nums[i]:
                if temp > answer:
                    answer = temp
                temp = 0
        return answer
