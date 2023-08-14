class Solution:
    def addDigits(self, num: int) -> int:
        # 38 = 3*10 + 8
        # 38 - 3 - 8 = 3*9
        # abc = a*100 + b * 10 + c
        # abc - a - b - c = a*99 + b*9
        # 결국 9의 배수만큼 빠져나감
        return 0 if num == 0 else (num - 1) % 9 + 1
