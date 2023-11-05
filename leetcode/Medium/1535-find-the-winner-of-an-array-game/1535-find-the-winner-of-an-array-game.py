class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        max_item = max(arr)
        queue = deque(arr[1:])
        curr = arr[0]
        wins = 0
        while queue:
            opp = queue.popleft()
            if curr > opp:
                queue.append(opp)
                wins += 1
            else:
                queue.append(opp)
                curr = opp
                wins = 1
            if curr == max_item or wins == k:
                return curr