class Solution:
    def getFactor(self, n):
        n_sqrt = int(n**1 / 2) + 1
        factorset = set()
        for i in range(2, n_sqrt):
            while n % i == 0:
                factorset.add(i)
                n //= i
        if n > 1:
            factorset.add(n)
        return len(factorset)

    def maximumScore(self, nums: List[int], k: int) -> int:
        mod = 10**9+7
        arr = [(i, self.getFactor(x), x) for i, x in enumerate(nums)]
        n = len(nums)
        left, right = [-1]*n, [n]*n

        left_stack, right_stack = [], []
        for idx, prime_num, num in arr:
            while left_stack and left_stack[-1][0] < prime_num:
                left_stack.pop()
            left[idx] = left_stack[-1][1] if left_stack else -1
            left_stack.append((prime_num, idx))

        for idx, prime_num, num in arr[::-1]:
            while right_stack and right_stack[-1][0] <= prime_num:
                right_stack.pop()
            right[idx] = right_stack[-1][1] if right_stack else n
            right_stack.append((prime_num, idx))
        
        arr.sort(key=lambda x:-x[2])
        ans = 1

        for idx, prime_num, num in arr:
            l, r = left[idx], right[idx]
            cnt = (idx-l)*(r-idx)
            if cnt <= k:
                ans = ans * pow(num, cnt, mod) % mod
                k -= cnt
            else:
                ans = ans * pow(num, k, mod) % mod
                break

        return ans