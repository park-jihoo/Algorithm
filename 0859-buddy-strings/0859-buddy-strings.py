class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        # same string and have duplicate letter
        if s == goal:
            return Counter(s).most_common()[0][1] > 1
        # different length -> wrong
        if not len(s) == len(goal):
            return False
        # different string
        change = []
        for idx in range(len(s)):
            if s[idx] != goal[idx] and len(change) == 0:
                change.append((s[idx], goal[idx]))
            elif s[idx] != goal[idx] and len(change) == 1:
                change.append((goal[idx], s[idx]))
            elif s[idx] != goal[idx]:
                return False
        return len(change) == 2 and change[0] == change[1]
