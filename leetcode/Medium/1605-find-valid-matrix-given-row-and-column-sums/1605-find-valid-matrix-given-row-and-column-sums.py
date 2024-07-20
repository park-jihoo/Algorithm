class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        rowheap, colheap = [(val, idx) for idx, val in enumerate(rowSum) if val != 0],[(val, idx) for idx, val in enumerate(colSum) if val != 0]
        ans = [[0]*len(colSum) for _ in range(len(rowSum))]
        while rowheap or colheap:
            rowmin, rowidx = heapq.heappop(rowheap)
            colmin, colidx = heapq.heappop(colheap)
            ans[rowidx][colidx] = min(rowmin, colmin)
            if rowmin > colmin:
                heapq.heappush(rowheap, (rowmin - colmin, rowidx))
            elif colmin > rowmin:
                heapq.heappush(colheap, (colmin - rowmin, colidx))

        return ans