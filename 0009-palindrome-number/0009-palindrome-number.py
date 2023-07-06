class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        k = int(str(x)[::-1])
        return k==x