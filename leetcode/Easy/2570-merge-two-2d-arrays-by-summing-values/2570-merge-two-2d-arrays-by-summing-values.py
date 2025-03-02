class Solution:
    def mergeArrays(
        self, nums1: List[List[int]], nums2: List[List[int]]
    ) -> List[List[int]]:
        cnt = Counter()
        for idx, val in nums1:
            cnt[idx] += val
        for idx, val in nums2:
            cnt[idx] += val
        return sorted([[key, val] for key, val in cnt.items()], key=lambda x: x[0])
