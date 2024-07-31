class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        n = len(books)
        dp = [float('inf') for _ in range(n+1)]
        dp[0] = 0
        for i in range(1, n+1):
            maxwid = shelfWidth
            maxh = 0
            j = i-1
            while j >=0 and maxwid - books[j][0] >= 0:
                maxwid -= books[j][0]
                maxh = max(maxh, books[j][1])
                dp[i] = min(dp[i], dp[j] + maxh)
                j -= 1
        return dp[-1]