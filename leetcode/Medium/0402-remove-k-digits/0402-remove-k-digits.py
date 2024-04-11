import sys

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for n in num:
            while stack and int(stack[-1]) > int(n) and k:
                stack.pop()
                k -= 1
            stack.append(str(n))
        while k:
            stack.pop()
            k -= 1
        if len(stack) == 0:
            return "0"
        sys.set_int_max_str_digits(100000)
        return str(int("".join(stack)))