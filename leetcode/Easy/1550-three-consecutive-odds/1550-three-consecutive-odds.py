class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        con = 0
        for num in arr:
            con = (con + 1) if num % 2 else 0
            if con == 3:
                return True
        return False
