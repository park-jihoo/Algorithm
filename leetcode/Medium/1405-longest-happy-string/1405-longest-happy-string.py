class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        # s doesn't contain any of "aaa", "bbb", "ccc" as a substring
        heap = [(-a, 'a'), (-b, 'b'), (-c, 'c')]
        heapq.heapify(heap)
        ans = ""
        while heap:
            cnt, ch = heapq.heappop(heap)
            cnt = -cnt
            if len(ans) >= 2 and ans[-1] == ch and ans[-2] == ch:
                if not heap:
                    break
                tmpcnt, tmpch = heapq.heappop(heap)
                if tmpcnt < 0:
                    ans += tmpch
                if tmpcnt < -1:
                    heapq.heappush(heap, (tmpcnt + 1, tmpch))
                heapq.heappush(heap, (-cnt, ch))
            elif cnt > 0:
                cnt -= 1
                ans += ch
                if cnt > 0:
                    heapq.heappush(heap, (-cnt, ch))
        return ans