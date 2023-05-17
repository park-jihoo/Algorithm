# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        l, cur = [], head
        while cur:
            l.append(cur.val)
            cur = cur.next
        l1, l2 = l[:len(l)//2], list(reversed(l[len(l)//2:]))
        return max([a+b for a, b in zip(l1, l2)])