class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 1:
            return True
        f = [_ for _ in range(0, n)]
        num = [1] * n
        
        def getf(x: int) -> int:
            if f[x] == x:
                return x
            f[x] = getf(f[x])
            return f[x]
        
        def merge(x: int, y: int):
            x, y = getf(x), getf(y)
            if x == y:
                return
            if num[x] < num[y]:
                x, y = y, x
            f[y] = x
            num[x] += num[y]
            
        have = {}
        for i in range(0, n):
            x = nums[i]
            if x == 1:
                return False
            d = 2
            while d * d <= x:
                if x % d == 0:
                    if d in have:
                        merge(i, have[d])
                    else:
                        have[d] = i
                    while x % d == 0:
                        x //= d
                d += 1
            if x > 1:
                if x in have:
                    merge(i, have[x])
                else:
                    have[x] = i
        return num[getf(0)] == n
        