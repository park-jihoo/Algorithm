# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new_head = ListNode(0)
        curr = new_head
        while head:
            if head.val == 0 and head.next is not None:
                curr.next = ListNode(0)
                curr = curr.next
            elif head.val != 0:
                curr.val += head.val
            head = head.next
        return new_head.next