# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head and head.next:
            temp = head.next
            temp.next, head = head, temp.next
            temp.next.next = self.swapPairs(head)
            return temp
        return head
