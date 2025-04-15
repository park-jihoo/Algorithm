class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        hashmap = {nums2[i]: i for i in range(n)}
        indices = [hashmap[num] for num in nums1]
        left, right = SortedList(), SortedList()
        lc, rc = [], []
        for i in range(n):
            lc.append(left.bisect_left(indices[i]))
            left.add(indices[i])
        for i in range(n - 1, -1, -1):
            rc.append(len(right) - right.bisect_left(indices[i]))
            right.add(indices[i])
        return sum(lc[i] * rc[n - 1 - i] for i in range(n))
