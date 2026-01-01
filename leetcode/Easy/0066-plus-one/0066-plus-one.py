class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if not digits[len(digits)-1] == 9:
            digits[len(digits)-1]+=1
        elif len(digits)==1:
            return [1,0]
        else:
            digits = self.plusOne(digits[:len(digits)-1])
            digits.append(0)
        return digits