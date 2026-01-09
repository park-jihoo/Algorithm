# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def dfs(self, root):
        if not root:
            return 0, None
        l1, l2 = self.dfs(root.left)
        r1, r2 = self.dfs(root.right)
        if l1 > r1:
            return l1 + 1, l2
        elif l1 < r1:
            return r1 + 1, r2
        return l1 + 1, root

    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        return self.dfs(root)[1]
