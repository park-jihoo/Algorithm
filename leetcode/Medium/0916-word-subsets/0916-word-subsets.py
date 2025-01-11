class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        max_freq = Counter()
        for word in words2:
            word_count = Counter(word)
            for char, count in word_count.items():
                max_freq[char] = max(max_freq[char], count)
        return [word for word in words1 if all(Counter(word)[char] >= max_freq[char] for char in max_freq)]