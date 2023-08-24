class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result, cur, cnt = [], [], 0
        
        def justify_line(cur, cnt, maxWidth):
            spaces_needed = maxWidth - cnt
            if len(cur) == 1:
                return cur[0] + ' ' * spaces_needed
            base_spaces = spaces_needed // (len(cur) - 1)
            extra_spaces = spaces_needed % (len(cur) - 1)
            justified_line = cur[0]
            for i in range(1, len(cur)):
                spaces = base_spaces + (1 if i <= extra_spaces else 0)
                justified_line += ' ' * spaces + cur[i]
            return justified_line
        
        for word in words:
            if cnt + len(word) + len(cur) > maxWidth:
                result.append(justify_line(cur, cnt, maxWidth))
                cur, cnt = [], 0
            cur.append(word)
            cnt += len(word)
        
        result.append(' '.join(cur).ljust(maxWidth))
        return result
