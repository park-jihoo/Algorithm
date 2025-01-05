class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        # line sweeping algorithm
        ops = []
        for start, end, direction in shifts:
            d = 2 * direction - 1
            ops.extend([(start, d), (end+1, -d)])
        ops.sort()
        ans = []
        pref = ii = 0
        for i, c in enumerate(s):
            while ii < len(ops) and ops[ii][0] == i:
                pref += ops[ii][1]
                ii += 1
            ans.append(chr((ord(c) - ord('a') + pref)%26 + ord('a')))
        return ''.join(ans)