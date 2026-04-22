class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        ans = []
        for q in queries:
            for d in dictionary:
                diff = 0
                for i in range(len(q)):
                    if q[i] != d[i]:
                        diff += 1
                if diff <= 2:
                    ans.append(q)
                    break
        return ans