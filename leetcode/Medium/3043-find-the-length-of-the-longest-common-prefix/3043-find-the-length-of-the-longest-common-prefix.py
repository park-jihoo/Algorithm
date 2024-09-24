class Trie:
    def __init__(self):
        self.head = {}

    def add(self, word):
        cur = self.head
        for ch in word:
            if ch not in cur:
                cur[ch] = {}
            cur = cur[ch]
            cur["*"] = True

    def common_prefix(self, word):
        cur = self.head
        for idx, ch in enumerate(word):
            if ch not in cur:
                return word[:idx]
            cur = cur[ch]
        if "*" in cur:
            return word
        return ""


class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        trie = Trie()
        for word in arr1:
            trie.add(str(word))
        ans = 0
        for word in arr2:
            ans = max(ans, len(trie.common_prefix(str(word))))
        return ans
