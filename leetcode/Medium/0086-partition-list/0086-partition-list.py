# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        smaller = ListNode(0)
        greater = ListNode(0)
        curr = head
        curr_s = smaller
        curr_g = greater
        while curr:
            if curr.val < x:
                curr_s.next = ListNode(curr.val)
                curr_s = curr_s.next
            else:
                curr_g.next = ListNode(curr.val)
                curr_g = curr_g.next
            curr = curr.next
        curr_s.next = greater.next
        return smaller.next