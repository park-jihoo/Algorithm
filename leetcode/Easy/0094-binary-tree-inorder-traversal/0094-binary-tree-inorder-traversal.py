# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        result = []
        def help(node):
            if node is None:
                return
            help(node.left)
            result.append(node.val)
            help(node.right)
        help(root)
        return result