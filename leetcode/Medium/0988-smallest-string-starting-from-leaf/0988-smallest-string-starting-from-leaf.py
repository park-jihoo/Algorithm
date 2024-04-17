# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recursion(self, root):
        left, right = [], []
        if root.left is not None:
            left.extend(self.recursion(root.left))
        if root.right is not None:
            right.extend(self.recursion(root.right))
        if len(left) + len(right) == 0:
            return [chr(ord('a')+root.val)]
        return [x + chr(ord('a')+root.val) for x in left+right]

    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        return min(self.recursion(root))