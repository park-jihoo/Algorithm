class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        num_split = [len(y) for y in "".join([str(x) for x in nums]).split("0")]
        if len(num_split) == 0:
            return 0
        elif len(num_split) == 1:
            return num_split[0] - 1
        answer = num_split[0]
        for i in range(1, len(num_split)):
            answer = max(answer, num_split[i] + num_split[i - 1])
        return answer
