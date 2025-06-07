class Solution:
    def clearStars(self, s: str) -> str:
        buckets = [[] for _ in range(26)]
        ans = []
        for ch in s:
            if ch != "*":
                ans.append(ch)
                buckets[ord(ch) - 97].append(len(ans) - 1)
            else:
                for i in range(26):
                    if buckets[i]:
                        idx = buckets[i].pop()
                        ans[idx] = None
                        break
        return "".join(c for c in ans if c is not None)
