# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        one = head
        two = head.next
        while one != two:
            if not two or not two.next:
                return False
            one = one.next
            two = two.next.next
        return True
