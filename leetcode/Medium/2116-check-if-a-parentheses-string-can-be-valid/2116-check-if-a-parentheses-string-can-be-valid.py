class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s) % 2 == 1:
            return False
        opn = 0
        for i in range(len(s)):
            if s[i] == '(' or locked[i] == '0':
                opn+=1
            else:
                opn -= 1
            if opn < 0:
                return False
        cse = 0
        for i in range(len(s)-1, -1, -1):
            if s[i] == ')' or locked[i] == '0':
                cse+=1
            else:
                cse -= 1
            if cse < 0:
                return False
        return True