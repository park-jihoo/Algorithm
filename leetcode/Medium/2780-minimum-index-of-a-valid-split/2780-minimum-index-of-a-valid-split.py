class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        d, z = Counter(nums).most_common(1)[0]
        for zz, i in enumerate((i for i, v in enumerate(nums) if v == d), 1):
            if zz * 2 > i + 1 and (z - zz) * 2 > len(nums) - i - 1:
                return i

        return -1
