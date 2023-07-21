class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        # 드디어 easy 나왔네
        answer = []
        greatest = max(candies)
        for ppl in candies:
            if ppl + extraCandies >= greatest:
                answer.append(True)
            else:
                answer.append(False)
        return answer
