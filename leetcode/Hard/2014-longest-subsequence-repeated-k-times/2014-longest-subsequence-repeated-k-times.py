class PositionIndex:
    def __init__(self, s):
        self.char_pos = defaultdict(list)
        for i, c in enumerate(s):
            self.char_pos[c].append(i)

    def is_k_repeated_subseq(self, pattern, k):
        idx = -1
        for _ in range(k):
            for c in pattern:
                if c not in self.char_pos:
                    return False
                lst = self.char_pos[c]
                i = bisect_right(lst, idx)
                if i == len(lst):
                    return False
                idx = lst[i]
        return True

class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        counter = Counter(s)
        valid_chars = sorted([c for c in counter if counter[c] >= k], reverse=True)

        pos_index = PositionIndex(s)
        queue = []
        
        heapq.heappush(queue, "")

        best = ""

        while queue:
            curr = heapq.heappop(queue)
            for c in valid_chars:
                new_seq = curr + c
                if pos_index.is_k_repeated_subseq(new_seq, k):
                    if len(new_seq) > len(best) or (len(new_seq) == len(best) and new_seq > best):
                        best = new_seq
                    if len(new_seq) < 7:
                        heapq.heappush(queue, new_seq)
        return best