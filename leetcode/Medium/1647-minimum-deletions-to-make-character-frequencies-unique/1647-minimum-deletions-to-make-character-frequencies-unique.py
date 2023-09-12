class Solution:
    def minDeletions(self, s: str) -> int:
        counter = Counter(s)
        deletion = 0
        used_freq = set()
        for char, freq in counter.items():
            while freq > 0 and freq in used_freq:
                freq -= 1
                deletion += 1
            used_freq.add(freq)
        return deletion