class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        c = Counter(s)
        c = sorted(c.items(),key = lambda i: i[0])
        ans = ""
        stack = [c.pop()]
        while stack:
            ch, num = stack.pop()
            if num <= repeatLimit:
                ans += ch * num
                if c:
                    stack.append(c.pop())
            else:
                ans += ch * repeatLimit
                num = num - repeatLimit
                stack.append((ch,num))
                if c:
                    ans += c[-1][0]
                    nums = c[-1][1] - 1
                    char = c[-1][0]
                    c[-1] = (char, nums)
                    if c[-1][1] == 0:
                        c.pop()
                else:
                    break
        return ans