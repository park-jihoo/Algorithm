# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        idset = set()
        now = head
        while now is not None:
            if id(now) in idset:
                return now
            idset.add(id(now))
            now = now.next
        return None
