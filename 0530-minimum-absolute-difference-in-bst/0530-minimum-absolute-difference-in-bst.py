# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder(self, order, root):
        if root is None:
            return
        self.inorder(order, root.left)
        order.append(root.val)
        self.inorder(order, root.right)

    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        values = []
        self.inorder(values, root)
        answer = float("inf")
        for idx in range(len(values) - 1):
            answer = min(answer, values[idx + 1] - values[idx])
        return answer
