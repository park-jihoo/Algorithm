class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        wordCounter = Counter()
        for word in words:
            wordCounter += Counter(list(word))
        for a, count in wordCounter.most_common():
            if count % len(words) != 0:
                return False
        return True
