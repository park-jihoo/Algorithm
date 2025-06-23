class Solution:
    def kMirror(self, k: int, n: int) -> int:
        def ispal(s):
            return s==s[::-1]
        def tobase(num,base):
            res=''
            while num>0:
                res=str(num%base)+res
                num//=base
            return res
        def genpal():
            leng=1
            while True:
                start=10**(leng-1) if leng>1 else 1
                end=10**leng
                for half in range(start,end):
                    s=str(half)
                    yield int(s+s[-2::-1])
                for half in range(start,end):
                    s=str(half)
                    yield int(s+s[::-1])
                leng+=1
        count=0
        total=0
        for i in genpal():
            if ispal(tobase(i,k)):
                total+=i
                count+=1
                if count==n:
                    break
        return total