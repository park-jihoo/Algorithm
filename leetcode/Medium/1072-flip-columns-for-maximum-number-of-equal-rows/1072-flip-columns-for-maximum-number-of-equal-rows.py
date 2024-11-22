class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        cnt = Counter()
        for row in matrix:
            cur, c, s = row[0], 1, ""
            for idx in range(1, len(row)):
                if row[idx] != cur:
                    s += str(c)
                    cur, c = row[idx], 0
                else:
                    c += 1
            cnt[s] +=1

        return cnt.most_common()[0][1]