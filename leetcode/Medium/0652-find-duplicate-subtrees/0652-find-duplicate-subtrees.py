# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import Counter


class Solution:
    def recursive(self, root):
        if root is None:
            return ""
        string = (
            str(root.val)
            + "/"
            + self.recursive(root.left)
            + "/"
            + self.recursive(root.right)
        )
        self.count[string] += 1
        if self.count[string] == 2:
            self.answer.append(root)
        return string

    def findDuplicateSubtrees(
        self, root: Optional[TreeNode]
    ) -> List[Optional[TreeNode]]:
        self.answer = []
        self.count = Counter()
        self.recursive(root)
        return self.answer
