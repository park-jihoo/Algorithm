class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        tickets = deque(tickets)
        ans = 0
        while tickets[k] > 0:
            n = tickets.popleft() - 1
            ans += 1
            if n > 0:
                tickets.append(n)
            if k == 0 and n == 0:
                break
            k = (k - 1) if k > 0 else (len(tickets) - 1)
        return ans