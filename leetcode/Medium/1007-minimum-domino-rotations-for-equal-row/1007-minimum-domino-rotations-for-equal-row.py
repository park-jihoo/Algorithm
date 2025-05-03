class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        key = Counter(chain(tops, bottoms)).most_common(1)[0][0]
        top, bottom = 0, 0
        for t, b in zip(tops, bottoms):
            if t != key and b != key:
                return -1
            top += int(t != key)
            bottom += int(b != key)
        return min(top, bottom)