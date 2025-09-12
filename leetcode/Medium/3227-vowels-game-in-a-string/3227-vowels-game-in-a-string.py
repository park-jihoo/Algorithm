class Solution:
    def doesAliceWin(self, s: str) -> bool:
        cnt = Counter(s)
        vowels = cnt["a"] + cnt["e"] + cnt["i"] + cnt["o"] + cnt["u"]
        if vowels == 0:
            return False
        return True
