class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        left, right = Counter(s[:len(s)//2]), Counter(s[len(s)//2:])
        left_cnt, right_cnt = 0, 0
        for char, cnt in left.most_common():
            if char in 'aeiouAEIOU':
                left_cnt += cnt
        for char, cnt in right.most_common():
            if char in 'aeiouAEIOU':
                right_cnt += cnt
        return left_cnt == right_cnt