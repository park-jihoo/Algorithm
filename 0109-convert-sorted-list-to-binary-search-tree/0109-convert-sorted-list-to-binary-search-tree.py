# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if head is None:
            return None
        if head.next is None:
            return TreeNode(val = head.val)
        now = head
        mid = head
        mid2 = head
        while now is not None and now.next is not None:
            now = now.next.next
            mid2 = mid
            mid = mid.next
        answer = TreeNode(val = mid.val)
        mid2.next = None
        answer.left = self.sortedListToBST(head)
        answer.right = self.sortedListToBST(mid.next)
        return answer