class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        c = Counter(hand)
        while c:
            num = min(c)
            cons = Counter(range(num, num + groupSize))
            print(cons, c)
            if len(cons - c) > 0:
                return False
            c -= cons

        return True
