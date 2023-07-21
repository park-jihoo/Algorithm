class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if flowerbed == [0]:
            return n <= 1
        elif len(flowerbed) == 1:
            return n == 0

        if flowerbed[0] == 0 and flowerbed[1] == 0:
            n -= 1
            flowerbed[0] = 1
        l = len(flowerbed)

        for i in range(1, l - 1):
            if flowerbed[i - 1] == 0 and flowerbed[i] == 0 and flowerbed[i + 1] == 0:
                flowerbed[i] = 1
                n -= 1

        if flowerbed[l - 2] == 0 and flowerbed[l - 1] == 0:
            n -= 1
            flowerbed[l - 1] = 1

        return n <= 0
