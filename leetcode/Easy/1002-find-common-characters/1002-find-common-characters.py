class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        ans = reduce(lambda a, b: Counter(a) & Counter(b), words, Counter(words[0]))
        return ans.elements()
