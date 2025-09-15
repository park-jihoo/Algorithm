class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        if len(brokenLetters) == 0:
            return len([x for x in text.split()])
        return len([x for x in text.split() if re.match(rf"^[^{brokenLetters}]+$", x)])
