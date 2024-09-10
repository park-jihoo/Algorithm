# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        while curr.next:
            newnode = ListNode(val=math.gcd(curr.val, curr.next.val), next=curr.next)
            curr.next = newnode
            curr = curr.next.next
        return head