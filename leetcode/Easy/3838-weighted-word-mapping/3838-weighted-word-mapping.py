class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        return "".join(
            [
                chr(ord("z") - sum(weights[ord(c) - ord("a")] for c in word) % 26)
                for word in words
            ]
        )
