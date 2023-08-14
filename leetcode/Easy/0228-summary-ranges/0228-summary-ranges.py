class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return []
        answer = []
        start, end = nums[0], nums[0]
        for i in range(0, len(nums) - 1):
            if nums[i] + 1 != nums[i + 1]:
                end = nums[i]
                if start == end:
                    answer.append(str(end))
                else:
                    answer.append(str(start) + "->" + str(end))
                start = nums[i + 1]
        end = nums[len(nums) - 1]
        if start == end:
            answer.append(str(end))
        else:
            answer.append(str(start) + "->" + str(end))
        return answer
