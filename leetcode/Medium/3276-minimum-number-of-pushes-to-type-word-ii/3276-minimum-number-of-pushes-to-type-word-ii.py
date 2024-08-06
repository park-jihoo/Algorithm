class Solution:
    def minimumPushes(self, word: str) -> int:
        # 2 ~ 9 mapping, minimum number of pushes needed
        ans = 0
        for idx, (key, val) in enumerate(Counter(word).most_common()):
            ans += val * (1 + idx // 8)
        return ans