class Solution:
    def bestClosingTime(self, customers: str) -> int:
        cur = customers.count("Y")
        opt = cur
        ans = 0
        for idx, status in enumerate(customers):
            if status == "Y":
                cur -= 1
            else:
                cur += 1
            if cur < opt:
                ans = idx + 1
                opt = cur
        return ans
