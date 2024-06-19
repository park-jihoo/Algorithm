class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        # m bouquet -> k adjacent flowers
        # ith flower bloom in the bloomDay[i] -> len(bloomDay) = n
        n = len(bloomDay)
        if m * k > n:
            return -1
        minVal, maxVal = min(bloomDay), max(bloomDay)
        ans = maxVal

        while minVal <= maxVal:
            mid = (minVal + maxVal) // 2
            cnt, bqt, adj = 0, 0, False
            for i in range(n):
                if bloomDay[i] <= mid:
                    if cnt == 0:
                        adj = True
                        cnt += 1
                    elif adj:
                        cnt += 1
                else:
                    cnt = 0
                    adj = False
                if cnt == k:
                    bqt += 1
                    cnt, adj = 0, False
            if bqt >= m:
                ans = min(ans, mid)
                maxVal = mid - 1
            else:
                minVal = mid + 1

        return ans