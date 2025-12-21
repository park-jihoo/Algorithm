class Solution:
    def minDeletionSize(self, strs):
        def is_sorted(A):
            return all(A[i] <= A[i + 1] for i in range(len(A) - 1))

        ans = 0
        cur = [""] * len(strs)

        for col in zip(*strs):
            cur2 = cur[:]
            for i, letter in enumerate(col):
                cur2[i] = cur2[i] + letter

            if is_sorted(cur2):
                cur = cur2
            else:
                ans += 1

        return ans
