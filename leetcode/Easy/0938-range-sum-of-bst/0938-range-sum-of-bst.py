# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        ans = 0
        if root is None:
            return 0
        if root.val <= high and root.val >= low:
            ans += root.val
        ans += self.rangeSumBST(root.left, low, high)
        ans += self.rangeSumBST(root.right, low, high)
            
        return ans