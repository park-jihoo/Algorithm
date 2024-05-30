class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        # equal XOR -> 전체가 0이어야 함
        ans = 0
        for i in range(len(arr)):
            xor = arr[i]
            for j in range(i+1, len(arr)):
                xor ^= arr[j]
                if not xor == 0:
                    continue
                ans += (j - i)
        return ans