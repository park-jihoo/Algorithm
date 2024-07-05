# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        ans = []
        curr, idx = head, 1
        minval = float('inf')
        while curr.next.next:
            if (curr.val < curr.next.val and curr.next.val > curr.next.next.val) or (curr.val > curr.next.val and curr.next.val < curr.next.next.val):
                if ans:
                    minval = min(minval, idx - ans[-1])
                ans.append(idx)
            curr = curr.next
            idx += 1
        if len(ans) < 2:
            return [-1, -1]
        return [minval, ans[-1] - ans[0]]