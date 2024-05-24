class Solution:
    def subsets(self, words):
        ans = []
        n = len(words)
        for i in range(2**n):
            sub = Counter()
            for j in range(n):
                if (i >> j) % 2 == 1:
                    sub += Counter(words[j])
            ans.append(sub)
        return ans

    def getScore(self, word, score):
        ans = 0
        for key, val in word.items():
            ans += score[ord(key) - ord("a")] * val
        return ans

    def maxScoreWords(
        self, words: List[str], letters: List[str], score: List[int]
    ) -> int:
        letter_count = Counter(letters)
        words_subset = self.subsets(words)
        ans = 0
        for word in words_subset:
            if word <= letter_count:
                ans = max(ans, self.getScore(word, score))
        return ans
