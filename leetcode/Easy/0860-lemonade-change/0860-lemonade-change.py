class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        purse = Counter()
        for bill in bills:
            purse[bill] += 1
            if bill == 10:
                if purse[5] == 0:
                    return False
                purse[5] -= 1
            if bill == 20:
                if purse[5] == 0:
                    return False
                if purse[10] > 0:
                    purse[10] -= 1
                    purse[5] -= 1
                    continue
                if purse[5] >= 3:
                    purse[5] -= 3
                    continue
                return False
        return True