# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.lst = []

    def search(self, node, level):
        if node is None:
            return
        if level == len(self.lst):
            self.lst.append(node.val)
        else:
            self.lst[level] += node.val
        self.search(node.left, level+1)
        self.search(node.right, level+1)

    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        self.search(root, 0)
        return self.lst.index(max(self.lst)) + 1