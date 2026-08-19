class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        ans = 0
        c = defaultdict(int)
        for r, s in reservedSeats:
            if 1 < s < 10:
                c[r] |= 1 << (s - 2)
        return (n - len(c)) * 2 + sum(
            0 in (r & 15, r & 60, r & 240) for r in c.values()
        )
