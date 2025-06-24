class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        val, ans = [], set()
        for i in range(len(nums)):
            if nums[i] == key:
                val.append(i)
        for x in val:
            ans.update(set(range(max(0, x-k), min(len(nums), x+k+1))))
        return sorted(list(ans))