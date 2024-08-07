class Solution:
    def threedigits(self, num):
        one = {1: "One", 2:"Two", 3:"Three", 4:"Four",5:"Five",6:"Six",7:"Seven",8:"Eight",9:"Nine"}
        tenth ={10:"Ten", 11:"Eleven", 12:"Twelve",13:"Thirteen",15:"Fifteen",18:"Eighteen", 20:"Twenty", 30:"Thirty", 40:"Forty", 50:"Fifty", 60:"Sixty", 70:"Seventy",80:"Eighty",90:"Ninety"}
        ans = ""
        if num >= 100:
            ans += one[num//100] + " Hundred"
        num %= 100
        if num == 0:
            return ans
        if num < 10:
            return ans + " " + one[num]
        elif num in tenth.keys():
            return ans + " " + tenth[num]
        elif 14 <= num < 20:
            return ans + " " + one[num-10]+"teen"
        else:
            div, mod = divmod(num, 10)
            return ans + " " + tenth[div*10] + " " + one[mod]
        return ans.strip()

    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
        d, n = deque([]), 0
        while num:
            d.appendleft(self.threedigits(num%1000))
            num //=1000
            n += 1
        ans = ""
        digits = [" Billion", " Million", " Thousand", " "][-n:]
        for s, d in zip(d, digits):
            if s:
                ans += s.strip() + " " + d.strip() + " "
        return ans.strip()