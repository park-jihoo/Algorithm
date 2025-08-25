class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        r, c=len(mat), len(mat[0])
        ans=[0]*(r*c)
        flip, idx=0, 0
        for d in range(r+c-1):
            if flip==0:
                i=min(d, r-1)
                j=d-i
                while i>=0 and j<c:
                    ans[idx]=mat[i][j]
                    i-=1
                    j+=1
                    idx+=1
            else:
                j=min(d, c-1)
                i=d-j
                while j>=0 and i<r:
                    ans[idx]=mat[i][j]
                    i+=1
                    j-=1
                    idx+=1
            flip=1-flip
        return ans  