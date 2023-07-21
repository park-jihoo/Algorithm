class Solution:
    def compress(self, chars: List[str]) -> int:
        num = 1
        compressed = []
        for i, char in enumerate(chars):
            if i == 0:
                compressed.append(char)
                continue
            elif char == chars[i - 1]:
                num += 1
            elif num == 1:
                compressed.append(char)
            else:
                num_list = list(str(num))
                compressed += num_list
                compressed.append(char)
                num = 1
            if i == len(chars) - 1 and num != 1:
                num_list = list(str(num))
                compressed += num_list
        for i in range(len(compressed)):
            chars[i] = compressed[i]
        chars = chars[0 : len(compressed)]
        return len(chars)
