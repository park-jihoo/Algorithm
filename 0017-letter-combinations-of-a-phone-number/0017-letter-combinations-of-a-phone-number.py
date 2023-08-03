class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dictionary = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        if len(digits) == 0:
            return []
        answer = []
        for d in list(digits):
            answer.append(dictionary[d])
        return [''.join(x) for x in itertools.product(*answer)]