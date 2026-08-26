class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        if s.count("1") < k:
            return ""

        left = 0
        count_one = 0
        res = ""

        for right in range(len(s)):
            if s[right] == "1":
                count_one += 1

            while count_one > k or (left <= right and s[left] == "0"):
                if s[left] == "1":
                    count_one -= 1
                left += 1

            if count_one == k:
                current = s[left : right + 1]

                if (
                    not res
                    or len(current) < len(res)
                    or (len(current) == len(res) and current < res)
                ):
                    res = current

        return res
