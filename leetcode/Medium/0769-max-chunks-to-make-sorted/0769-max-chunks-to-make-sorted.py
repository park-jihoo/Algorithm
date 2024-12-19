class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        pref_max = list(accumulate(arr, max))
        suff_min = list(accumulate(arr[::-1], min))[::-1]
        return sum(
            int(i == 0 or suff_min[i] > pref_max[i - 1]) for i in range(len(arr))
        )
