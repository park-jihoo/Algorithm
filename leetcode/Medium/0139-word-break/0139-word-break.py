class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        q = deque([0])
        visited = set()
        while q:
            start = q.popleft()
            if start == len(s):
                return True
            for end in range(start + 1, len(s) + 1):
                if end in visited:
                    continue
                if s[start:end] in wordDict:
                    q.append(end)
                    visited.add(end)
        return False
