class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        ans = [-1] * len(rains)
        full, z = dict(), []
        for idx, lake in enumerate((rains)):
            if lake == 0:
                z.append(idx)
            else:
                if lake in full:
                    left, right = 0, 0
                    while right < len(z) and z[right] <= full[lake]:
                        right += 1
                    if right == len(z):
                        return []
                    ans[z[right]] = lake
                    z.pop(right)
                full[lake] = idx
        for d in z:
            ans[d] = 1
        
        return ans