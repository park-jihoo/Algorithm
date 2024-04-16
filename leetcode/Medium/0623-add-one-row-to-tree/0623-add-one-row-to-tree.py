# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(
        self, root: Optional[TreeNode], val: int, depth: int
    ) -> Optional[TreeNode]:
        if root is None:
            return None
        if depth == 1:
            return TreeNode(val=val, left=root)
        elif depth == 2:
            temp1, temp2 = root.left, root.right
            root.left = TreeNode(val=val, left=temp1)
            root.right = TreeNode(val=val, right=temp2)
            return root
        else:
            temp1, temp2 = root.left, root.right
            root.left = self.addOneRow(temp1, val, depth - 1)
            root.right = self.addOneRow(temp2, val, depth - 1)
            return root
