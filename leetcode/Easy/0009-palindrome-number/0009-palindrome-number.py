class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x)[::-1] == str(x)

class Solution2:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        k = int(str(x)[::-1])
        return k==x