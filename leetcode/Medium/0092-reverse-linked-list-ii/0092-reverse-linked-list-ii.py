# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(
        self, head: Optional[ListNode], left: int, right: int
    ) -> Optional[ListNode]:
        temp = ListNode(-1)  # sentinel
        prev = temp
        temp.next = head
        for i in range(left - 1):
            prev = prev.next
        cur = prev.next
        for i in range(right - left):
            ptr = prev.next
            prev.next = cur.next
            cur.next = cur.next.next
            prev.next.next = ptr
        return temp.next
