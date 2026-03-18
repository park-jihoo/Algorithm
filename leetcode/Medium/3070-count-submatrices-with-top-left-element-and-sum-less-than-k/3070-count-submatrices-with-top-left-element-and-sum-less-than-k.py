class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        pref = [list(accumulate(row)) for row in grid]
        prefs = list(
            accumulate(pref, lambda x, y: [x[i] + y[i] for i in range(len(x))])
        )
        return len([x for x in list(chain.from_iterable(prefs)) if x <= k])
