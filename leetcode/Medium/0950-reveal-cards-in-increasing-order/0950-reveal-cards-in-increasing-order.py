class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        ans = deque([])
        deck.sort()
        while deck:
            ans.rotate(1)
            ans.appendleft(deck.pop())
        return ans