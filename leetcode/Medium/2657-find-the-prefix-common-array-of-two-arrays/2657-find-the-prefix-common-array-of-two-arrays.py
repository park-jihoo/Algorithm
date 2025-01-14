class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        cnta, cntb, ans = set(), set(), []
        for a, b in zip(A, B):
            cnta.add(a)
            cntb.add(b)
            ans.append(len(cnta & cntb))
        return ans
