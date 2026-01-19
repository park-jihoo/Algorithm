class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        ans = 0
        m, n = len(mat), len(mat[0])
        pref = [list(accumulate(x)) for x in mat]

        def check(side):
            for i in range(0, m-side+1):
                for j in range(0, n - side + 1):
                    tmp = 0
                    for row in range(side):
                        tmp += pref[row+i][j+side-1] - (pref[row+i][j-1] if j else 0)
                    if tmp <= threshold:
                        return True
            return False

        left, right = 0, min(m, n)
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                ans = max(ans, mid)
                left = mid + 1
            else:
                right = mid - 1

        return ans