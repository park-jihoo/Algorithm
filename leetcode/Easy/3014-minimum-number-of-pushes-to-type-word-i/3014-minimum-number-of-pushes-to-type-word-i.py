class Solution:
    def minimumPushes(self, word: str) -> int:
        ans, cnt = 0, Counter(word)
        n = len(cnt.keys())

        for idx, (ch, cn) in enumerate(cnt.most_common()):
            ans += (1 + idx // 8) * cn
        return ans
