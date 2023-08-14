from collections import deque


class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)
        dq, rq = deque([]), deque([])
        for idx, s in enumerate(list(senate)):
            if s == "R":
                rq.append(idx)
            else:
                dq.append(idx)
        while rq and dq:
            ri, di = rq.popleft(), dq.popleft()
            if ri < di:
                rq.append(ri + n)
            else:
                dq.append(di + n)
        return "Radiant" if len(rq) > len(dq) else "Dire"
