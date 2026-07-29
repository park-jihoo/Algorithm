class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        freq = Counter(s)
        half = {c:freq[c] //2 for c in freq}
        mid = ""
        
        for c in freq:
            if freq[c] & 1:
                mid = c 
                break
        total = sum(half.values())
        chars = sorted(half.keys())
        LIMIT = 10** 6 + 1
        
        def countperm(cnt, rem):
            res = 1
            left = rem
            for c in chars:
                x = cnt[c]
                if x:
                    res *= comb(left,x)
                    if res> LIMIT:
                        return LIMIT
                    left -= x
            return res
        
        if countperm(half, total) <k:
            return ""
        left = []
        while total:
            for c in chars:
                if half[c] == 0:
                    continue
                half[c] -= 1
                ways = countperm(half, total -1)
                if ways >= k:
                    left.append(c)
                    total -=1
                    break
                else:
                    k -= ways
                    half[c] += 1
        left ="".join(left)
        return left + mid + left[::-1]