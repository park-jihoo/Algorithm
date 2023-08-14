# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.maxlen = 0

    def zig(self, root, isleft, length):
        if isleft and root.right is not None:
            self.zig(root.right, False, length + 1)
        if not isleft and root.left is not None:
            self.zig(root.left, True, length + 1)
        # start path
        if isleft and root.left is not None:
            self.zig(root.left, True, 1)
        if not isleft and root.right is not None:
            self.zig(root.right, False, 1)
        self.maxlen = max(self.maxlen, length)

    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 0
        if root.left is not None:
            self.zig(root.left, True, 1)
        if root.right is not None:
            self.zig(root.right, False, 1)
        return self.maxlen
