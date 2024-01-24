# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def pseudoPalindromicPaths(self, root: Optional[TreeNode]) -> int:
        def preorder(node, path_set):
            nonlocal count
            if node:
                path_set ^= {node.val}
                if node.left is None and node.right is None:
                    if len(path_set) <= 1:
                        count += 1
                else:
                    preorder(node.left, path_set.copy())
                    preorder(node.right, path_set.copy())

        count = 0
        preorder(root, set())
        return count
