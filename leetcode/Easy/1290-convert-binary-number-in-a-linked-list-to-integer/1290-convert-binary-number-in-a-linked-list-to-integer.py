# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        curr, ans = head, 0
        while curr:
            ans = ans*2 + curr.val
            curr = curr.next
        return ans