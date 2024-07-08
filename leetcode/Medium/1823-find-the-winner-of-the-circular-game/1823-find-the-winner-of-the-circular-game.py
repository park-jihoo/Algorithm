class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        ppl, curr = deque(list(range(1, n + 1))), 0
        while len(ppl) > 1:
            curr += 1
            can = ppl.popleft()
            if curr != k:
                ppl.append(can)
            else:
                curr = 0
        return ppl[0]
