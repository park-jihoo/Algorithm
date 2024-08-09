class Solution:
    def isMagicSquare(self, arr: List[int]) -> bool:
        x = arr[0] + arr[3] + arr[6]
        y = arr[1] + arr[4] + arr[7]
        z = arr[2] + arr[5] + arr[8]
        a = arr[0] + arr[1] + arr[2]
        b = arr[3] + arr[4] + arr[5]
        c = arr[6] + arr[7] + arr[8]
        c1 = arr[0] + arr[4] + arr[8]
        c2 = arr[2] + arr[4] + arr[6]

        return x == y == z == a == b == c == c1 == c2

    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        l,u, mss = 0,0,0
        hm, rm = len(grid), len(grid[0])

        if hm<3 or rm<3:
            return 0

        while u + 2 != hm:
            l = 0
            while l+2 != rm:
                res = []
                for y in range(u,u+3):
                    for i in range(l,l+3):
                        res.append(grid[y][i])
                if set(res) == set(range(1,10)) and self.isMagicSquare(res):
                    mss += 1
                l+=1
            u += 1 

        return mss