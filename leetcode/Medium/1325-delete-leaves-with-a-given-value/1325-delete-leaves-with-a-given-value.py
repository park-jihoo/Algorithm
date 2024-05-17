# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root, target):
        if root is None:
            return None
        if root.left is None and root.right is None:
            if root.val == target:
                self.flag = True
                return None
            else:
                return root
        else:
            return TreeNode(
                val=root.val,
                left=self.dfs(root.left, target),
                right=self.dfs(root.right, target),
            )

    def removeLeafNodes(
        self, root: Optional[TreeNode], target: int
    ) -> Optional[TreeNode]:
        self.flag = False
        root = self.dfs(root, target)
        while self.flag:
            self.flag = False
            root = self.dfs(root, target)
        return root
