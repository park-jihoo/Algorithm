class Solution:
    def spiralMatrixIII(
        self, rows: int, cols: int, rStart: int, cStart: int
    ) -> List[List[int]]:
        def key(a):
            x, y = a
            x, y = x - rStart, y - cStart
            return (
                max(abs(x), abs(y)),
                -((math.atan2(-1, 1) - math.atan2(x, y)) % (math.pi * 2)),
            )

        return sorted([(i, j) for i in range(rows) for j in range(cols)], key=key)
