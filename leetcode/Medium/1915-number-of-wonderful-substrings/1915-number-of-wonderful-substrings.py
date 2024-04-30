class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        count = [0] * 1024
        result = 0
        prefix_xor = 0
        count[prefix_xor] = 1
        for char in word:
            char_idx = ord(char) - ord('a')
            prefix_xor ^= 1 << char_idx
            result += count[prefix_xor]
            for i in range(10):
                result += count[prefix_xor ^ (1<<i)]
            count[prefix_xor] += 1
        return result