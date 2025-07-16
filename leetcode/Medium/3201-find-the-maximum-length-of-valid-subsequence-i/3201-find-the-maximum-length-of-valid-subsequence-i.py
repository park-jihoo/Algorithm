class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        odds = [x for x in nums if x % 2 == 1]
        evens = [x for x in nums if x % 2 == 0]
        oe, eo = [], []
        for x in nums:
            if x % 2 == 1:
                if not oe or oe[-1] % 2 == 0:
                    oe.append(x)
                if eo and eo[-1] % 2 == 0:
                    eo.append(x)
            if x % 2 == 0:
                if not eo or eo[-1] %2 == 1 :
                    eo.append(x)
                if oe and oe[-1] % 2 == 1:
                    oe.append(x)
        return max(len(odds), len(evens), len(oe), len(eo))