from collections import defaultdict


class Solution:
    def __init__(self):
        self.parents = []

    def isSimilar(self, a, b):
        cnt = 0
        for s1, s2 in zip(a, b):
            if s1 != s2:
                cnt += 1
            if cnt >= 3:
                return False
        return True

    def findParent(self, a):
        if self.parents[a] == a:
            return a
        self.parents[a] = self.findParent(self.parents[a])
        return self.parents[a]

    def union(self, a, b):
        a, b = self.findParent(a), self.findParent(b)
        if a < b:
            self.parents[b] = a
        else:
            self.parents[a] = b

    def numSimilarGroups(self, strs: List[str]) -> int:
        strs = list(set(strs))
        dic = defaultdict(list)

        # combination groups
        for s in strs:
            vec = [0] * 26
            for c in s:
                vec[ord(c) - 97] += 1
            dic[tuple(vec)].append(s)
        ans = 0

        for _, ss in dic.items():
            self.parents = list(range(len(strs)))
            for i in range(len(strs)):
                for j in range(i + 1, len(strs)):
                    if self.isSimilar(ss[i], ss[j]):
                        self.union(i, j)
            for i in range(len(self.parents)):
                self.findParent(i)
            ans += len(set(self.parents))
        return ans
