class Solution:
    def canChange(self, start: str, target: str) -> bool:
        if start.replace("_", "") != target.replace("_", ""):
            return False
        startd = {"L" : [], "R" : []}
        targetd = {"L" : [], "R" : []}
        for idx, (c1, c2) in enumerate(zip(start, target)):
            if c1 == 'L' or c1 == 'R':
                startd[c1].append(idx)
            if c2 == 'L' or c2 == 'R':
                targetd[c2].append(idx)
        for l1, l2 in zip(startd["L"], targetd["L"]):
            if l1 < l2:
                return False
        for r1, r2 in zip(startd["R"], targetd["R"]):
            if r1 > r2:
                return False
        return True