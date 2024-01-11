# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getmin(self, root):
        if root is None:
            return float("inf")
        return min(root.val, self.getmin(root.left), self.getmin(root.right))

    def getmax(self, root):
        if root is None:
            return 0
        return max(root.val, self.getmax(root.left), self.getmax(root.right))

    def getdiff(self, root):
        if root is None:
            return 0
        minval, maxval = self.getmin(root), self.getmax(root)
        diff = max(abs(root.val - minval), abs(root.val - maxval))
        return diff

    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        return max(
            self.getdiff(root),
            self.maxAncestorDiff(root.left),
            self.maxAncestorDiff(root.right),
        )
