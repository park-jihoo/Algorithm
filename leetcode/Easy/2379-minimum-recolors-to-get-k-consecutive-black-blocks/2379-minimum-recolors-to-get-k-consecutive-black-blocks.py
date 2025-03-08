class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        tmp = blocks[:k].count("W")
        ans = tmp
        for i in range(0, len(blocks) - k):
            if blocks[i] == "W":
                tmp -= 1
            if blocks[i + k] == "W":
                tmp += 1
            ans = min(tmp, ans)
        return ans
