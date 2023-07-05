# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        idx = 0
        s1, s2 = head, head
        while s1.next:
            s1 = s1.next
            idx+=1
        s1 = head

        for i in range(idx):
            if i < k - 1:
                s1 = s1.next
            if i <= idx - k:
                s2 = s2.next
        
        temp = s1.val
        s1.val = s2.val
        s2.val = temp

        return head