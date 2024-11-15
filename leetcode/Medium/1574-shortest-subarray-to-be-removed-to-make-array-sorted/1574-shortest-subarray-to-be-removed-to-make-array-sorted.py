class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        n = len(arr)
        start, end = 1, n-2
        a1, a2 = 1, 1
        inc, dec = [arr[0]], [arr[n-1]]
        while start < n and arr[start-1]<=arr[start]:
            a1 += 1
            inc.append(arr[start])
            start+=1
        if inc == arr:
            return 0
        
        while end > 0 and arr[end] <= arr[end+1]:
            a2 += 1
            dec.append(arr[end])
            end-=1
        
        ans = max(a1, a2)
        for idx in range(len(dec) - 1, -1, -1):
            ans = max(ans, bisect_right(inc, dec[idx])+idx+1)
        
        return n - ans