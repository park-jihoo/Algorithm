# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        ans = [[-1] * n for _ in range(m)]
        curr, i, j, didx = head, 0, 0, 0
        while curr:
            ans[i][j] = curr.val
            ni, nj = i + d[didx][0], j + d[didx][1]
            if 0 <= ni < m and 0 <= nj < n and ans[ni][nj] == -1:
                i, j = ni, nj
            else:
                didx = (didx + 1) % 4
                i, j = i + d[didx][0], j + d[didx][1]
            curr = curr.next
        return ans
