class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        ans = 0
        cntr = Counter(words)
        odds, evns = [], []
        for word, cnt in cntr.items():
            if word[0] == word[1] and cnt % 2 == 1:
                odds.append(word)
                cntr[word] -= 1
        cntr = Counter(cntr.elements())
        visited = set()
        for word in cntr.keys():
            if word not in visited:
                rev = word[::-1]
                visited.add(rev)
                if word == rev:
                    ans += cntr[word] * 2
                else:
                    ans += 4 * min(cntr[word], cntr[rev])
        return ans + 2 if odds else ans