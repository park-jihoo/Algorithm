class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly = set()
        ugly.add(1)
        cur = 1
        for i in range(n):
            cur = min(ugly)
            ugly.remove(cur)
            ugly.add(cur * 2)
            ugly.add(cur * 3)
            ugly.add(cur * 5)
        return cur
