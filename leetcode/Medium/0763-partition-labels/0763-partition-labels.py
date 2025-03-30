class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        pos = [-1] * 26
        for idx, ch in enumerate(s):
            pos[ord(ch) - ord("a")] = idx
        ans, st, ed = [], 0, -1
        for idx, ch in enumerate(s):
            ed = max(ed, pos[ord(ch) - ord("a")])
            if idx == ed:
                ans.append(ed - st + 1)
                st = idx + 1
        return ans
