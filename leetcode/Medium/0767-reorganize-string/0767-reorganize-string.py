class Solution:
    def reorganizeString(self, s: str) -> str:
        ans = []
        pq = [(-count, char) for char, count in Counter(s).items()]
        heapify(pq)
        while pq:
            co, ch = heappop(pq)
            if not ans or ch != ans[-1]:
                ans.append(ch)
                if co + 1 != 0:
                    heappush(pq, (co+1, ch))
            else:
                if not pq:
                    return ''
                co2, ch2 = heappop(pq)
                ans.append(ch2)
                if co2+1 != 0:
                    heappush(pq, (co2+1, ch2))
                heappush(pq, (co, ch))
        return ''.join(ans)