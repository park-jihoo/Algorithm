class Solution:
    def smallestNumber(self, pattern: str) -> str:
        stack, temp = [], []
        for idx, ch in enumerate(pattern):
            stack.append(str(idx + 1))
            if ch == "I":
                while stack:
                    num = stack.pop()
                    temp.append(num)

        temp.append(str(len(pattern) + 1))
        while stack:
            num = stack.pop()
            temp.append(num)
        return "".join(temp)
