# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = ListNode(0, head)
        prev, curr = temp, temp.next
        while prev and curr:
            if curr.val >= 5:
                prev.val += 1
            curr.val = (curr.val*2)%10
            prev, curr = prev.next, curr.next
        return temp if temp.val == 1 else temp.next