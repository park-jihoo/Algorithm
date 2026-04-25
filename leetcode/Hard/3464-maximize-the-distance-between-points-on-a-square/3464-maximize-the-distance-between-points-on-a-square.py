class Solution:
    def maxDistance(self, side: int, points: List[List[int]], k: int) -> int:
        pts = [[], [], [], []]
        for x, y in points:
            if x == 0 and y != 0:
                pts[0].append((x, y))
            elif x != 0 and y == side:
                pts[1].append((x, y))
            elif x == side and y != side:
                pts[2].append((x, y))
            else:
                pts[3].append((x, y))
        pts[0].sort()
        pts[1].sort()
        pts[2].sort(reverse=True)
        pts[3].sort(reverse=True)
        points = [p for line in pts for p in line]

        def check(d):
            dq = deque([(points[0][0], points[0][1], points[0][0], points[0][1], 1)])
            best = 1
            for nx, ny in points[1:]:
                mx, my, ln = nx, ny, 1
                while dq and abs(nx - dq[0][0]) + abs(ny - dq[0][1]) >= d:
                    cx, cy, ox, oy, l = dq.popleft()
                    if l + 1 >= ln and abs(nx - ox) + abs(ny - oy) >= d:
                        mx, my, ln = ox, oy, l + 1
                        best = max(best, ln)
                dq.append((nx, ny, mx, my, ln))
            return best >= k

        l, r = 0, side
        while l <= r:
            m = (l + r) // 2
            if check(m):
                l = m + 1
            else:
                r = m - 1

        return r
