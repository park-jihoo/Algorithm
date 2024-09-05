class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        # add n rolls and make mean as 'mean'
        aim = mean * (len(rolls) + n) - sum(rolls)
        div, mod = divmod(aim, n)
        if div <= 0 or div > 6 or (div == 6 and mod > 0):
            return []
        return [div] * (n - mod) + [div + 1] * mod
