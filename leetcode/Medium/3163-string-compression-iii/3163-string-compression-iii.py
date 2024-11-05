class Solution:
    def compressedString(self, word: str) -> str:
        comp = ""
        cnt, tmp = 1, word[0]
        for idx, ch in enumerate(word):
            if idx == 0:
                continue
            if ch != tmp or cnt == 9:
                comp += str(cnt) + str(tmp)
                cnt, tmp = 0, ch
            cnt += 1
        comp += str(cnt) + str(tmp)
        return comp
