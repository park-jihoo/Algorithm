class Trie:
    def __init__(self):
        self.head = {}

    def add(self, word):
        cur = self.head
        for ch in word:
            if ch not in cur:
                cur[ch] = {}
            cur = cur[ch]
            cur["*"] = cur.get("*", 0) + 1

    def score(self, word):
        cur = self.head
        ans = 0
        for ch in word:
            ans += cur[ch]["*"]
            cur = cur[ch]
        return ans


class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        trie = Trie()
        for word in words:
            trie.add(word)
        return [trie.score(word) for word in words]
