class WordDictionary:

    def __init__(self):
        self.words = defaultdict(set)

    def addWord(self, word: str) -> None:
        self.words[len(word)].add(word)

    def search(self, word: str) -> bool:
        if "." not in word:
            return word in self.words[len(word)]
        for v in self.words[len(word)]:
            for idx, char in enumerate(word):
                if char != v[idx] and char != ".":
                    break
            else:
                return True
        return False




# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)