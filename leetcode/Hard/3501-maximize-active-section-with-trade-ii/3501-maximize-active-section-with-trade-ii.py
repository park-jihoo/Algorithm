class SparseTable:
    def __init__(self, data: list):
        self.st = [list(data)]
        i, N = 1, len(self.st[0])
        while 2 * i <= N + 1:
            pre = self.st[-1]
            self.st.append(
                [max(pre[j], pre[j + i]) for j in range(N - 2 * i + 1)]
            )
            i <<= 1

    def query(self, begin: int, end: int):
        if begin > end:
            return 0
        lg = (end - begin + 1).bit_length() - 1
        return max(self.st[lg][begin], self.st[lg][end - (1 << lg) + 1])


class Solution:
    def maxActiveSectionsAfterTrade(
        self, s: str, queries: List[List[int]]
    ) -> List[int]:
        n = len(s)
        cnt1 = s.count("1")

        zeroBlocks = []
        blockLeft = []
        blockRight = []

        i = 0
        while i < n:
            st = i

            while i < n and s[i] == s[st]:
                i += 1

            if s[st] == "0":
                zeroBlocks.append(i - st)
                blockLeft.append(st)
                blockRight.append(i - 1)

        m = len(zeroBlocks)
        if (
            m < 2
        ):  # continuous 0 blocks less than 2 segments, return the answer directly
            return [cnt1] * len(queries)

        tmpSum = [zeroBlocks[i] + zeroBlocks[i + 1] for i in range(m - 1)]
        st = SparseTable(tmpSum)
        ans = []

        for l, r in queries:
            i = bisect_left(blockRight, l)
            j = bisect_right(blockLeft, r) - 1

            # at most 1 continuous block of 0s within the substring
            if i > m - 1 or j < 0 or i >= j:
                ans.append(cnt1)
                continue

            firstLen = (
                blockRight[i] - max(blockLeft[i], l) + 1
            )  # actual length of the first consecutive block of 0s in the substring

            lastLen = (
                min(blockRight[j], r) - blockLeft[j] + 1
            )  # actual length of the last consecutive block of 0s in the substring

            # exactly 2 consecutive 0 blocks within the substring
            if i + 1 == j:
                bestGain = firstLen + lastLen
                ans.append(cnt1 + bestGain)
                continue

            val1 = firstLen + zeroBlocks[i + 1]

            val2 = zeroBlocks[j - 1] + lastLen

            val3 = st.query(i + 1, j - 2)

            bestGain = max(val1, val2, val3)

            ans.append(cnt1 + bestGain)

        return ans