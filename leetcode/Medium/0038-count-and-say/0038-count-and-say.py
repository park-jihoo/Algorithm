class Solution:
    def countAndSay(self, n: int) -> str:
        countlist = ["1"]
        for i in range(1, n):
            temp = ""
            now, cnt = -1, -1
            for a in list(countlist[i - 1]):
                if cnt == -1:
                    now = int(a)
                    cnt = 1
                elif not a == str(now):
                    temp += str(cnt) + str(now)
                    now = int(a)
                    cnt = 1
                else:
                    cnt += 1
            temp += str(cnt) + str(now)
            countlist.append(temp)
        return countlist[n - 1]
