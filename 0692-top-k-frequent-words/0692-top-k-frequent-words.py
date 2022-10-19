from collections import Counter

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        wordCounter = Counter(words)
        sortedWordCounter = sorted(wordCounter.items(), key = lambda x:(-x[1], x[0]))
        return [x[0] for x in sortedWordCounter][:k]