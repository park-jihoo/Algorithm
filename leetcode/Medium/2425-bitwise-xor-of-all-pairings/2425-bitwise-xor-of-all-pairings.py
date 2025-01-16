class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        ans1, ans2 = 0, 0
        if len(nums1) % 2 == 1:
            ans1 = reduce(lambda a, b: a ^ b, nums2, 0)
        if len(nums2) % 2 == 1:
            ans2 = reduce(lambda a, b: a ^ b, nums1, 0)
        return ans1^ans2