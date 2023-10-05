class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = Counter(nums).most_common()
        answer = []
        for num, cnt in count:
            if cnt > len(nums) // 3:
                answer.append(num)
        return answer
