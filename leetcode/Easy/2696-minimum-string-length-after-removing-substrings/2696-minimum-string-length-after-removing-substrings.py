class Solution:
    def minLength(self, s: str) -> int:
        prev_len = len(s)
        while True:
            s = re.sub(r"AB|CD", "", s)
            if len(s) == prev_len:
                return len(s)
            prev_len = len(s)
        return 0