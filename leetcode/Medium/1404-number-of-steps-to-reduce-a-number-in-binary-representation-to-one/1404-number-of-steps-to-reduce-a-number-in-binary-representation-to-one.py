class Solution:
    def numSteps(self, s: str) -> int:
        # even -> divide by 2
        # odd -> add 1
        ans = 0
        lst = list(s)
        while lst:
            if lst[-1] == "0":
                lst.pop()
            elif len(lst) == 1 and lst[0] == "1":
                return ans
            else:
                while lst and lst[-1] == "1":
                    lst.pop()
                    ans += 1
                if len(lst) == 0:
                    ans += 1
                    return ans
                else:
                    lst[-1] = "1"
            ans += 1
        return ans