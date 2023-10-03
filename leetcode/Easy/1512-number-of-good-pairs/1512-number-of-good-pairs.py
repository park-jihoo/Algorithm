class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        counter = Counter(nums).most_common()
        answer = 0
        for key, value in counter:
            answer += (value * (value - 1)) // 2
        return answer