# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.helper(root, [0])
        return root

    def helper(self, root, node_sum):
        if root is None:
            return
        self.helper(root.right, node_sum)
        node_sum[0] += root.val
        root.val = node_sum[0]
        self.helper(root.left, node_sum)
