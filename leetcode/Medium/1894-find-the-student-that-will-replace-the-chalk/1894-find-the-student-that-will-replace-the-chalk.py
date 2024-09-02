class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        a = sum(chalk)
        k %= a
        for idx, val in enumerate(chalk):
            if k < val:
                return idx
            k -= val
        return len(chalk) - 1