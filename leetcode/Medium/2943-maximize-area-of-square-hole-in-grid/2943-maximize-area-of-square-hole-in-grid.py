class Solution:
    def maximizeSquareHoleArea(
        self, n: int, m: int, hBars: List[int], vBars: List[int]
    ) -> int:
        def longCons(arr):
            m = {}
            res = 0
            for i in arr:
                if i in m:
                    continue
                l = m.get(i - 1, 0)
                r = m.get(i + 1, 0)
                f = l + r + 1
                res = max(res, f)
                m[i - l] = f
                m[i + r] = f
            return res

        s = min(longCons(hBars), longCons(vBars)) + 1
        return s * s
