class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort()
        
        prices, beauties = [], []
        max_beauty = 0
        
        for price, beauty in items:
            max_beauty = max(max_beauty, beauty)
            prices.append(price)
            beauties.append(max_beauty)
        ans = []
        
        for query in queries:
            idx = bisect_right(prices, query) - 1
            if idx >= 0:
                ans.append(beauties[idx])
            else:
                ans.append(0)
        
        return ans