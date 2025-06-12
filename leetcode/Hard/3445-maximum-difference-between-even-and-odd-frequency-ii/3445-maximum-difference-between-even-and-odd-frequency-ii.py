class Solution:
    def maxDifference(self, s: str, k: int) -> int:
        idx = [[] for i in range(5)] # index of char
        for i,c in enumerate(s):
            idx[int(c)].append(i)
        idx = [q for q in idx if len(q)] # remove empty
        n = len(s)
        for q in idx: q.append(n) #sentinel to simplify end case
        def sol(q1,q2): # max (odd q1 - even q2)
            # monotonic deque (alive time, val of q1-q2)
            que = [deque() for i in range(4)] # (odd,even)*(odd,even)
            prev = [inf]*4 # prefix alive minima 
            que[0].append((max(q1[0],q2[0],k-1),0))
            i=j=0; best = -inf
            curr = -1 # current right position
            # invariant: next q1 and next q2
            while q1[i]!=q2[j]: # end when both end (sentinel)
                if q1[i]<q2[j]: # next q1 enter 
                    if q1[i]>curr: curr=q1[i]
                    i += 1
                else: # next q2 enter
                    if q2[j]>curr: curr=q2[j]
                    j += 1
                # alive right position = before next coming
                right = min(q1[i],q2[j])-1  
                parity = (i&1)|((j&1)<<1) # prefix parity
                prev_p = parity^1 # diff bit0, same bit 1
                # wake up alive
                while que[prev_p] and que[prev_p][0][0]<=right:
                    _,prev[prev_p] = que[prev_p].popleft()
                best = max(best, i-j - prev[prev_p])
                # push (i-j)
                v = i-j
                # alive when curr+k and next i and next j
                if v<prev[parity] and ((not que[parity]) or v<que[parity][-1][1]):
                    que[parity].append((max(curr+k,q1[i],q2[j]),v))
            # while
            return best
        # end sol
        ans = -inf
        for q1,q2 in permutations(idx,2):
            ans = max(ans,sol(q1,q2))
        return ans