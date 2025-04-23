class Solution:
    def countLargestGroup(self, n: int) -> int:
        hashmap = Counter()
        for i in range(1, n+1):
            key = sum(int(x) for x in str(i))
            hashmap[key] += 1
        maxval = max(hashmap.values())
        cnt = sum(1 for v in hashmap.values() if v == maxval)
        return cnt