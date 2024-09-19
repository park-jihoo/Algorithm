class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        if expression.isdigit():
            return [int(expression)]
        ans = []
        for idx, val in enumerate(expression):
            if val in "-+*":
                left = self.diffWaysToCompute(expression[:idx])
                right = self.diffWaysToCompute(expression[idx + 1 :])
                for l in left:
                    for r in right:
                        if val == "+":
                            ans.append(l + r)
                        if val == "-":
                            ans.append(l - r)
                        if val == "*":
                            ans.append(l * r)
        return ans
